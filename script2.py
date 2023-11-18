# import pandas as pd
# import os

# folder_path = './Files'
# columns_to_extract = ['gene_name', 'gene_type', 'fpkm_unstranded']

# cumulative_data = pd.DataFrame()

# for filename in os.listdir(folder_path):
#     if filename.endswith('.csv'):
#         file_path = os.path.join(folder_path, filename)
#         print("Processing:", file_path)
        
#         try:
#             df = pd.read_csv(file_path, skiprows=[0, 1, 2, 3])
#             filtered_df = df[df['gene_type'] == 'protein_coding']
            
#             # Select only the required columns
#             filtered_df = filtered_df[columns_to_extract]
            
#             cumulative_data = cumulative_data.append(filtered_df, ignore_index=True)
#         except pd.errors.ParserError as e:
#             print("Error while reading CSV:", e)
#             continue

# cumulative_data.to_csv('cumulative_data.csv', index=False)
# print("Processing complete.")

import pandas as pd
import os

folder_path = './test'
columns_to_extract = ['gene_name', 'gene_type', 'fpkm_unstranded']

cumulative_data = pd.DataFrame()

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        print("Processing:", file_path)
        
        try:
            df = pd.read_csv(file_path)
            
            # Keep only the first-indexed row and reset the index
            df = df.iloc[[0]].reset_index(drop=True)
        except pd.errors.ParserError as e:
            print("Error while reading CSV:", e)
            continue

cumulative_data.reset_index(drop=True, inplace=True)  # Reset the index after processing all files
cumulative_data.to_csv('cumulative_data.csv', index=False)
print("Processing complete.")
