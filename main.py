import os
import glob
import json
import pandas as pd

data_dir = '/Users/krishnap/Desktop/2020-5-27/document_parses/'
pdf_dir = os.path.join(data_dir, "pdf_json")
pmc_dir = os.path.join(data_dir, "pmc_json")

pdf_list = os.listdir(pdf_dir)
print(f" Number of pdf papers: {len(pdf_list)}")

pmc_list = os.listdir(pmc_dir)
print(f" Number of pmc papers: {len(pmc_list)}")

csv_data = []
paper_count = 0
for file_path in glob.glob(pdf_dir + "/*.json"):
    with open(file_path, "r") as f:
        data = json.loads(f.read())
        paper_id = data["paper_id"]
        title = data["metadata"]["title"]
        if len(data["abstract"]) > 0:
            abstract = data["abstract"][0]["text"]
        else:
            abstract = ""
        body_text = data["body_text"]
        full_body_text = ""
        for paragraph in body_text:
            full_body_text = paragraph["text"] + "|"

        csv_data.append({"paper_id": paper_id, "title": title, "abstract": abstract, "body_text": full_body_text})

    paper_count += 1
    if paper_count == 1000:
        break

    pd.DataFrame(csv_data).to_csv("all_paper.csv", sep="\t")