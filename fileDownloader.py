import requests
import json
import csv
from io import StringIO
import os

try:
    os.makedirs("./Files")
except FileExistsError:
    pass


def get_file_id_from_case(case_id):
    print(f"Fetching data for Case ID: {case_id}...")

    # find the file UUID of the gene list of the given case
    files_endpt = "https://api.gdc.cancer.gov/files"

    # filter for the gene expression data of the particular case
    filters = {
        "op": "and",
        "content": [
            {
                "op": "=",
                "content": {
                    "field": "cases.case_id",
                    "value": case_id
                }
            },

            {
                "op": "in",
                "content": {
                    "field": "files.data_category",
                    "value": "Transcriptome Profiling"
                }
            },

            {
                "op": "in",
                "content": {
                    "field": "files.data_type",
                    "value": "Gene Expression Quantification"
                }
            },
        ]
    }

    params = {
        "filters": json.dumps(filters),
        "fields": "file_id",
        "format": "JSON",
        "size": 1
    }

    response = requests.get(files_endpt, params=params)

    file_id = json.loads(response.content.decode("utf-8"))["data"]["hits"][0]["file_id"]

    return file_id


def download_file(file_id, case_id):
    data_endpt = f"https://api.gdc.cancer.gov/data/{file_id}"

    # check if the file is open access
    # try:
    response = requests.get(data_endpt, headers={
                            "Content-Type": "application/json"})
    if response.content == b'{"message":"Your token is invalid or expired. Please get a new token from GDC Data Portal."}\n':
        print(f"{case_id} is a controlled file, can't download!!!")
        return

    tsv_content = response.content.decode('utf-8')
    tsv_io = StringIO(tsv_content)
    tsv_reader = csv.reader(tsv_io, delimiter='\t')

    file_name = f"./Files/{case_id}"
    csv_filepath = file_name + ".csv"

    with open(csv_filepath, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in tsv_reader:
            csv_writer.writerow(row)

    print(f"Downloaded and saved {case_id} as a CSV file.")

    # except:
    #     print(f"Error! Case ID: {case_id} could not be downloaded.")
    #     return


# obtain the case UUIDs from the text document
case_ids = []

with open("./case_uuids.txt", "r") as case_ids_file:
    for line in case_ids_file:
        if line[0].isalnum():
            case_ids.append(line.rstrip('\n'))

# download the gene list file for each case id
for case_id in case_ids:
    file_id = get_file_id_from_case(case_id)
    download_file(file_id, case_id)
