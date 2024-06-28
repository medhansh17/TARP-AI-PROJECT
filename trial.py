import os
import pandas as pd

input_folder = "./Files"
output_file = "./trial.csv"

gene_list =  [
    'CYP4Z2P', 'TCN1', 'DHRS2', 'COL9A1', 'HEPHL1', 'MYOSLID', 'MYBPHL', 'EPGN', 'LINC00941', 'FAM83A-AS1',
    'MUC4', 'KRT13', 'C8orf46', 'DMBT1', 'NCAN', 'TSPAN1', 'ZP2', 'FAM83A', 'MLC1', 'CCDC60', 'BMP1', 'KCNJ15',
    'ADGRF4', 'CYP4Z1', 'PADI1', 'CLCA2', 'STON2', 'SYTL5', 'AC244153.1', 'CAPNS2', 'KRT6C', 'MUCL1', 'COL5A3',
    'TFF1', 'AC008147.2', 'BPIFB1', 'AL358334.2', 'AC011294.1', 'ADRA1D', 'LIMA1', 'HTRA1', 'LINC01605', 'FAM212A',
    'LINC02568', 'CFI', 'LRRC31', 'CADPS', 'PTHLH', 'C9orf84', 'GPR1', 'CERCAM', 'ANKS4B', 'AL590644.1', 'MUC6',
    'NRP1', 'ADGRL3', 'THY1', 'AC004870.2', 'ADAMTS14', 'COL5A1', 'COL4A6', 'LRRC17', 'BBOX1-AS1', 'CHL1', 'SMIM3',
    'ADAMTS12', 'SPTSSB', 'CASC18', 'AC113346.1', 'SOX8', 'PLPPR3', 'GUCY1A2', 'COL1A1', 'AKAP1', 'PCDH7', 'PCDHB12',
    'MAB21L3', 'C2CD4A', 'COL7A1', 'GALNT10', 'FAM198A', 'ITGA3', 'EPHA8', 'Z99289.1', 'AC021087.4', 'P4HA3',
    'MAST4', 'PLXDC1', 'LINC01828', 'RASGRF2', 'AL356515.1', 'HTR7', 'ZNF385C', 'MMP2', 'CYP3A5', 'PHYHIP', 'SMIM31',
    'IYD', 'HOXB-AS3', 'SLC5A5', 'AC009041.2', 'EXTL1', 'C1QTNF6', 'CREG2', 'PLAC9', 'PRSS3', 'FAM19A3', 'COL1A2',
    'AC009078.3', 'SEMA3F', 'CCDC190', 'AP000844.2', 'AGR2', 'CTSK', 'POU3F1', 'MSC', 'AL035665.1', 'LINC01116',
    'AC110995.1', 'PCDHGC5', 'ARHGAP23', 'ECM1', 'SLC45A2', 'F3', 'LINC02532', 'AC005077.4', 'AKR1B10', 'SRPX',
    'GTF2IP7', 'ANKRD36C', 'AP001528.2', 'HOXA-AS2', 'MEG3', 'FRMD7', 'DHRS9', 'LRP1', 'VCAN', 'SPAAR', 'RFX8',
    'LINC01179', 'HOXD11', 'M'
]
genes_df = pd.DataFrame({'Gene': gene_list})

bl1=['a9bb8159-32f0-454c-a946-b3286a52b9d5.csv', 'b58ad350-5140-4fa8-bc2c-24bca8395f3a.csv', 'eb2dbb4f-66b6-4525-8323-431970f7a64e.csv', '324bcba2-f6a4-45a6-807c-215bdffcca21.csv', '99e32c59-aa73-43fa-88c9-399ddadb2c72.csv', '5cbf0aea-ebb4-4005-bdd5-14ef2dc6826c.csv', 'a78b04b4-2380-4803-963e-e4e633cd69ab.csv', 'c72cb184-462d-4009-9cdb-848782ff8a76.csv', '53886143-c1c6-40e9-88e6-e4e5e0271fc8.csv', 'b6633c36-7ce4-4b69-9bf6-30b64d46c66f.csv', 'cf9db1af-17f0-490e-8139-142bd704763a.csv', '72e486b8-a866-4916-b2e4-8b4bb5dcd92d.csv', '6412854a-f874-469e-9d1f-8bd3ae5bd41d.csv', '8183f0fb-2303-4d7b-bccd-55e5031fc7df.csv', 'dfaabd03-2d40-4422-b210-caf112ff4229.csv', '49717f75-0f2d-4e1c-9a12-f1cd7877b80a.csv', '05506f4c-e701-4a9d-ae06-97f066aade43.csv', 'a9b7d7fe-be31-4f71-afee-c1bfdf511888.csv', 'e9f4f373-37a5-48ad-a1a0-b0d47820111a.csv', 'b094e8b2-8ece-4b36-8025-18073a8b873c.csv', '016caf42-4e19-4444-ab5d-6cf1e76c4afa.csv', 'c70ee5e1-4703-4996-bb5c-f4cca0fb53ba.csv', '9938ce5c-e74e-446e-a932-f096f85cc3b1.csv', '972447aa-4332-47e7-bddd-2eb699dbb664.csv', '71f97b63-c970-44ee-98c2-e02e663d5a40.csv', '9848307d-1bd5-40c1-b655-a33297aaf74f.csv', '98e0b4de-52fc-4945-9bf5-11e29368f939.csv', 'd3d545b3-457f-4389-821f-704cb24aff7f.csv', '328dfcb0-b5ae-43f2-bc87-dad0ab3df9e7.csv', '4bf50455-9ab7-4521-a791-089f66d3b877.csv', '75b3fe55-1a63-426e-867e-2ef52f54778d.csv', '5a57dc25-d252-4b22-b192-4de630d7002f.csv', '4f608829-ffc4-4527-886e-6bc764ab29f5.csv', '30ec8b1f-28c4-4f46-8a1b-a8d51e558c7d.csv', '6b923e30-2ddc-407f-91b1-c202f1373fbb.csv', '7e1673f8-5758-4963-8804-d5e39f06205b.csv', 'f1692f4b-ce1b-4fc5-ac55-1022ecae0d1e.csv', 'f0d8a1fe-e313-44f1-99cc-b965cbeeff0e.csv', 'fc18d029-9be2-4fa0-9aef-6d647dc55f0b.csv', '97943d87-fed7-4f14-a0a7-c5bfee64c392.csv', '3886b4fb-ba22-4a50-b11a-a6893951f170.csv', '752ad011-79e0-494f-9868-98bf6feb28f8.csv', '4fba3deb-db94-44b5-a0f2-a575d270779e.csv', 'e0b1bcd2-1139-44b9-98b3-67bcf92bcc39.csv', '3558dec7-eae3-4a41-a217-266c6a4535fb.csv', '1d27253f-b036-44e7-a04d-8da5bbf57419.csv', '6429c443-8ac3-407f-bb9c-66420b904bbf.csv', '56033839-35d5-4d72-8b8c-400cb345263d.csv', '4da999a0-ef41-4a0b-b1d1-446b39cc855a.csv', 'd6f7afc0-1558-43ad-acb1-2b5311ed2264.csv', '65cac997-4d39-4501-85ec-4fcb328a8eb5.csv', '124b693c-77dc-4fa8-b703-54e8b5054a92.csv', 'c8f39325-5382-447c-9291-a6915fc978b8.csv', 'a82d0a57-4383-473d-b334-d13b278404b1.csv', '35bd694d-1dd2-466f-ab27-03320614b40e.csv', '398fb71b-ca83-44e7-bf0d-b1ca464b0283.csv', '23c31c2e-336c-4878-a476-cf8d811b4875.csv']

bl2= ['18d35983-ea6a-4b70-a209-9bef37595956', '3b7b9c1e-a84c-47ed-983c-9e4b00cbf01a', '5ed024e8-d05e-4c65-9441-eda9930ccc82', 'b2ecbc0f-2c30-4200-8d5e-7b95424bcadb', '8c09f413-e938-4f2e-a414-84f0e7fcfe41', 'dbf6f981-15cc-40ad-91ac-a66360405fbd', '98e709e7-e195-4b37-9537-f6081affb609', 'e8ea576b-eb16-44f7-b241-daefc1375388', 'd9fd2724-7db0-4af3-ac14-217bdfa5203f', '3e9f93c0-aa79-4b4c-bd6c-b3325912362a', 'a1da9db1-db11-4f4d-a249-c738db81b87e', '0685edd2-ce1c-4e0e-8dda-393139af4223', '23e7a78a-1d56-4ad1-9bb4-72ec0178aff2', '623befd6-0ca4-4a6c-9cf5-d9385c3b718f', 'eda6d2d5-4199-4f76-a45b-1d0401b4e54c', '3af31fcf-ad0c-4fd9-a8e3-10f9176b5e9d', '92b5de82-0221-4df1-8094-80f40c0bb4fa', 'c49e3b18-fd88-48f4-8b01-300692ceb367', '5a17dcd9-5ced-4a69-8069-23c7fd0649d1', 'aa4244a8-0454-4247-a1c3-357fd51746fa', 'ae65baeb-6b78-492a-8c63-bb7e93e83dc2', '4ac693e9-10f3-46b3-9d46-df3af7b0d259', 'd7308344-5bab-4073-bb4f-4d8cd8d7bd17', '89128dba-403f-4a96-bb3b-23ed0d5e2147', 'ef4cbd38-bc79-4d60-a715-647edd2ebe9e', '2a84997d-ccee-4f46-bea2-752534f26416', 'e3935ce4-64d3-4a66-ba11-d308b844b410', '521e2140-ae5b-456f-8699-97398d009687', '01674b2c-5cf2-478f-84a1-f69c39f47bd4', '359f12f9-5c41-48a4-85bc-fd7e307bf7d8', '88db1340-e4bf-451a-87c0-6e9168296f5e', '389e5b18-8f89-41a9-9fa5-efd4172836e2', '9087585f-e792-4f33-baaa-56ffe0f745be', 'e783e518-c1e5-4eac-8eaf-e2d65ccd9692']

lar= ['ccd4a24b-d8cc-4686-9dee-c98b0c5a8d21', '2192c1db-4718-4254-ba42-3ae7f30ad5a8', '295cf595-4a29-46a3-a0c5-e5f08f947031', '9d95a65b-e41d-4f93-92d4-99dce29ff40d', 'd2f2560c-ec80-4fea-9474-c47a2e85ea95', 'b7f74ae1-6f58-447c-be50-a7666eb19d9a', '376ffe63-efd7-42af-90e1-261255b28bb7', '3f834fa7-6d7b-4b85-98c0-5c55d55b6c95', '9416ff9b-6f29-4554-b04d-b537a3ae3969', '18eb4dfc-556f-4bf3-a411-4780209ed1e0', '20e8106b-1290-4735-abe4-7621e08e3dc8', 'db4bc6aa-2e7d-4bcb-8519-a455f624d33b', '6b960b58-28e1-41c6-bd6e-7e669c6aa4ef', '9d166970-07c8-4ca3-9cfa-ed0049df9ecc', 'ad18820b-a804-49c0-ba8a-86c09fa6bce2', 'b97bf89a-7a85-4eef-ae7e-f787aead1f0a', '2dc1cec9-925a-417f-9e21-3c2143e711b4', '70ab4f23-23c4-409f-a5cc-18a010c3a24e', '4d51159f-ab2f-40e3-a363-847c3654431e', '959ff069-8a49-4c9b-85c2-5291cac0acff', '1c40b84e-a0e3-429f-a48c-21566cf881c0', 'dcd5e079-813a-4c1a-b320-0931468d2bbc', '7f2a63e6-64d5-4be1-9814-e8416fc9e688', '791c5768-f0f5-4ab6-86eb-998e5c4b49e3', 'd8ecba6a-9fff-4993-a799-9a8d2aea524e', 'f06f09f3-8133-4a92-ac86-fbe64295e0d8', '408cb583-6dc3-4698-8bd2-e284042bd5ef', 'ac68d219-5670-4ddd-8df6-8aa7ad59e5c7', 'f2e28af9-c40e-41c4-9e82-205cca38f26a', '6e6b7742-a562-490b-bb72-04a5653852e4', 'b343bfe0-7c23-4c6a-8c84-9ee39db2ecda', '5700c1b3-922a-4401-8ab8-89028908d696', '66fa504c-4ae4-49ac-9355-1e063776dc0d', 'b8aefc48-4a6e-4254-a57f-5f688399b582', 'aa60fa8d-c374-40e0-af2d-b007701e67e3', 'c3a981c7-f148-4252-bd50-af8a49ec0df8', 'f81ac8a2-4ce6-439e-b027-1c0bfc88ceaa', '6ffd1b8c-6f0b-456a-9160-e0c8021e5897']

m =['a5b44d66-c162-46b5-9df2-86305f0385c5', '6644fd4e-d2fe-4785-a73c-0f36fcc740e2', '1c3610f7-e0aa-48d7-9a27-0dbaf6e244f9', '95c53f69-0f05-4348-822a-571f3d757001', '128d198e-9b22-427c-90db-3714455f3a17', 'a8e7d8a4-bbf0-496b-b387-8e014cfdcea6', 'deba32e4-0e68-4711-941b-3b63bd965afb', '3afa1e93-1df8-4e4c-aaa4-557463f4bb77', '0ec70e40-07df-461d-8ff9-351240a0d454', '57af5c72-0d60-4a6b-b1b4-ec6dab90f80f', '6fa2a667-9c36-4526-8a58-1975e863a806', '67c5f371-3fa9-47c5-8b15-c2dd9acc8519', 'ebc460c2-df88-4dc0-a2c0-aca8072b75ad', '546248b0-22a0-4b70-a437-76fb0a238a0d', 'baf1207d-7d1a-4cad-ba58-62c26be2415e', '13b860c3-8048-4dc9-9eb0-7480bc660837', '96312510-c126-485d-8109-ed81844a1dc3', '495f9eda-b9be-4eef-bae1-766a4bfbd68e', '58090433-d8d1-4499-a235-810c3e9d5b74', 'ab89bb2e-da84-4116-a8cd-49aad7bbfd4d', 'a6e11b30-3ae8-4dd1-b04c-a730c6a79746', '5fd9552a-c742-4388-940d-295d1107ae00', 'd093173f-08ab-4138-bf3c-399c45a6e163', '045c13ef-3db7-4adf-b0a3-23338f0479f3', '01eef340-598c-4205-a990-cec190ac2ca5', '08da7c4c-3067-4bcf-9d7a-78566df72e69', '6956473b-92e5-4069-a26b-b48e280e76f2', 'a482fc4c-ff1d-46a0-a968-7df06422cc4b', '790ff5db-b7f3-4946-aaed-305f66b1dd6a', '6c0066e3-96df-4870-bcd3-98cda64082e9', '786e8dbe-442e-4551-87b3-b4c333b04dd4', '747083ff-0703-431b-aad4-f2adff739516', 'a855c228-a263-44df-87a0-cbc32187e3f5', 'ccb22ecc-6e18-44b8-ad48-6ab51314b16e', '1549dc64-3dab-43fc-96e9-b07d520957e1', '0dca98b0-f43e-45b6-9a02-00092c78678c', 'a6edb6ca-ae9f-4da7-8ebe-92d83d2987fb', '91a2f2af-e4b1-4a0b-ab20-6a36ce63c533', '029ce650-5e5a-4100-8596-cd94300e7ef5', 'ac075bc0-1b59-4557-beea-541694faee03', 'a4c59287-1ad5-46a5-8040-e591e6ce064f', 'f55dd73d-8c36-440b-84e5-9aae53107775', '9f6be944-83de-42ab-8738-f0022f475e61', 'ea645243-df49-4466-a255-9f3d4321e357']


# Loop through files
for file in os.listdir(input_folder):
    if file.endswith(".csv"):
        print("Processing file:", file)
        input_file = os.path.join(input_folder, file)
        
        df = pd.read_csv(input_file, skiprows={0, 2, 3, 4, 5})
        
        # Rename the FPKM column
        fpkm_col_name = os.path.splitext(file)[0]
        df.rename(columns={'fpkm_unstranded': fpkm_col_name}, inplace=True)
        
        # Merge the FPKM values with the genes DataFrame based on 'Gene' column
        genes_df = pd.merge(genes_df, df[['gene_name', fpkm_col_name]], left_on='Gene', right_on='gene_name', how='left')
        genes_df.drop('gene_name', axis=1, inplace=True)  # Drop the extra 'gene_name' column from the merge
        unique_identifier = os.path.splitext(file)[0]
        # Rename the FPKM column back to file name
        genes_df.rename(columns={fpkm_col_name: os.path.splitext(file)[0]}, inplace=True)

        # Check if the unique identifier is in any of the lists and add the list name to the last row
        if unique_identifier in bl1:  # Remove last 4 characters (".csv")
            genes_df.loc[len(genes_df)] = ['bl1', unique_identifier]
        elif unique_identifier in bl2:
            genes_df.loc[len(genes_df)] = ['bl2', unique_identifier]
        elif unique_identifier in lar:
            genes_df.loc[len(genes_df)] = ['lar', unique_identifier]
        elif unique_identifier in m:
            genes_df.loc[len(genes_df)] = ['m', unique_identifier]
        else:
            print("File not matched with any subtype")
            print(unique_identifier)
# Save the combined DataFrame to the output file
genes_df.to_csv(output_file, index=False)
print(f"FPKM values extracted and saved to {output_file}")
