import csv

# Path to the CSV files
file1_path = "./swapped_fpkm_file.csv"
file2_path = "./scratch.csv"
output_path = "output.csv"

# Read data from file1.csv
with open(file1_path, 'r') as file1:
    reader1 = csv.reader(file1)
    data1 = list(reader1)

# Read data from file2.csv
with open(file2_path, 'r') as file2:
    reader2 = csv.reader(file2)
    data2 = list(reader2)

# Check if the number of rows in both files is the same
if len(data1) == len(data2):
    # Combine the data from both files
    combined_data = [row1 + [row2[0]] for row1, row2 in zip(data1, data2)]

    # Write the combined data to output.csv
    with open(output_path, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerows(combined_data)

    print(f"The data from {file2_path} has been added as the last column in {output_path}.")
else:
    print("Error: The number of rows in the two files is not the same.")
