import os
import pandas as pd
import numpy as np

input_folder = "./Files"
output_folder = "./output_files"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

error_file = []

for file in os.listdir(input_folder):
    if file.endswith(".csv"):
        try:
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, file)

            df = pd.read_csv(input_file, skiprows={0, 2, 3, 4, 5})

            stranded_first_col = 'stranded_first'
            stranded_second_col = 'stranded_second'

            df['log2fc'] = np.log2(df[stranded_first_col] + 1) - \
                np.log2(df[stranded_second_col] + 1)

            df.to_csv(output_file, index=False)

            print(
                f"Log2 fold change values calculated and saved to {output_file}")
        except Exception as e:
            print(f"Error processing file {file}: {e}")
            error_file.append(file)
print("/n/n")
for i in error_file:
    print(f"Error processing file {i}")
