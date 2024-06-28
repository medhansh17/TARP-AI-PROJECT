import os
import pandas as pd

input_folder = "./Files"
output_file = "./tpm_file_2.csv"

gene_list =  [
    'CYP4Z2P', 'TCN1', 'DHRS2', 'COL9A1', 'HEPHL1', 'MYOSLID', 'MYBPHL', 'EPGN', 'LINC00941', 'FAM83A-AS1',
    'MUC4', 'KRT13', 'DMBT1', 'NCAN', 'TSPAN1', 'ZP2', 'FAM83A', 'MLC1', 'CCDC60', 'BMP1', 'KCNJ15',
    'ADGRF4', 'CYP4Z1', 'PADI1', 'CLCA2', 'STON2', 'SYTL5', 'AC244153.1', 'CAPNS2', 'KRT6C', 'MUCL1', 'COL5A3',
    'TFF1', 'AC008147.2', 'BPIFB1', 'AL358334.2', 'AC011294.1', 'ADRA1D', 'LIMA1', 'HTRA1', 'LINC01605',
    'LINC02568', 'CFI', 'LRRC31', 'CADPS', 'PTHLH', 'GPR1', 'CERCAM', 'ANKS4B', 'MUC6',
    'NRP1', 'ADGRL3', 'THY1', 'AC004870.2', 'ADAMTS14', 'COL5A1', 'COL4A6', 'LRRC17', 'BBOX1-AS1', 'CHL1', 'SMIM3',
    'ADAMTS12', 'SPTSSB', 'CASC18', 'AC113346.1', 'SOX8', 'PLPPR3', 'GUCY1A2', 'COL1A1', 'AKAP1', 'PCDH7', 'PCDHB12',
    'MAB21L3', 'C2CD4A', 'COL7A1', 'GALNT10', 'ITGA3', 'EPHA8', 'Z99289.1', 'AC021087.4', 'P4HA3',
    'MAST4', 'PLXDC1', 'LINC01828', 'RASGRF2', 'AL356515.1', 'HTR7', 'ZNF385C', 'MMP2', 'CYP3A5', 'PHYHIP', 'SMIM31',
    'IYD', 'HOXB-AS3', 'SLC5A5', 'AC009041.2', 'EXTL1', 'C1QTNF6', 'CREG2', 'PLAC9', 'PRSS3', 'COL1A2',
    'AC009078.3', 'SEMA3F', 'CCDC190', 'AP000844.2', 'AGR2', 'CTSK', 'POU3F1', 'MSC', 'AL035665.1', 'LINC01116',
    'AC110995.1', 'PCDHGC5', 'ARHGAP23', 'ECM1', 'SLC45A2', 'F3', 'LINC02532', 'AC005077.4', 'AKR1B10', 'SRPX',
    'GTF2IP7', 'ANKRD36C', 'AP001528.2', 'HOXA-AS2', 'MEG3', 'FRMD7', 'DHRS9', 'LRP1', 'VCAN', 'SPAAR', 'RFX8',
    'LINC01179', 'HOXD11'
]

genes_df = pd.DataFrame({'Gene': gene_list})

for file in os.listdir(input_folder):
    if file.endswith(".csv"):
        print("Processing file:", file)
        input_file = os.path.join(input_folder, file)
        
        df = pd.read_csv(input_file, skiprows={0, 2, 3, 4, 5})
        
        # Rename the FPKM column
        tpm_col_name = os.path.splitext(file)[0]
        df.rename(columns={'tpm_unstranded': tpm_col_name}, inplace=True)
        
        # Merge the FPKM values with the genes DataFrame based on 'Gene' column
        genes_df = pd.merge(genes_df, df[['gene_name', tpm_col_name]], left_on='Gene', right_on='gene_name', how='left')
        genes_df.drop('gene_name', axis=1, inplace=True)  # Drop the extra 'gene_name' column from the merge

        # Rename the FPKM column back to file name
        genes_df.rename(columns={tpm_col_name: os.path.splitext(file)[0]}, inplace=True)

# Save the combined DataFrame to the output file
try:
    genes_df.to_csv(output_file, index=False)
    print(f"FPKM values extracted and saved to {output_file}")
except Exception as e:
    # Error handling
    print("Error:", e)
    # Handle the error according to your requirements

