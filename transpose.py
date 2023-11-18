import pandas as pd

# Reading the CSV file into a DataFrame
df = pd.read_csv('./fpkm_file_2.csv')

# Swapping index and columns
swapped_df = df.transpose()

# Assigning original index as columns and original columns as index
swapped_df.columns = df.index
swapped_df.index = df.columns

# Writing the swapped DataFrame back to a CSV file without the first row of index values
swapped_df.to_csv('swapped_fpkm_file.csv', header=False)


# Reading the CSV file into a DataFrame
df = pd.read_csv('./tpm_file_2.csv')

# Swapping index and columns
swapped_df = df.transpose()

# Assigning original index as columns and original columns as index
swapped_df.columns = df.index
swapped_df.index = df.columns

# Writing the swapped DataFrame back to a CSV file without the first row of index values
swapped_df.to_csv('swapped_tpm_file.csv', header=False)
