
import os
import glob
import json
import pandas as pd


data_dir = '/Users/krishnap/.spyder-py3/REU COVID-19'
file_path = os.path.join(data_dir, "all_paper.csv")

df = pd.read_csv(file_path, sep="\t", header=None)
print(df.head())

# =============================================================================
#
# "
# a='spread'
# with open('all_paper.csv') as f_obj:
# '    reader = csv.reader(f_obj, delimiter=',')
# '    for line in reader:
# '        print(line)
#         if a in str(line):
#             print(" ")
#         break
#
# =============================================================================

print(df.shape)

p_count = 0
for i in range(df.shape[0]):
    # df.iloc[i, 0]  index
    # df.iloc[i, 1] paper_id
    abstract = df.iloc[i, 3]
    title = df.iloc[i, 2]
    paragraphs = df.iloc[i, 4].split("|")
    # print(len(paragraphs))
    # print(paragraphs[0])

    paragraphs.append(abstract)
    paragraphs.append(title)

    for p in paragraphs:
        if "spread" in p:
            print(p)
            p_count += 1
        break
    # process each paragraph
    if p_count >= 1:
        break

spread_list = ["spread", "transmission" , "widespread", "circulate", "disperse", "transmit", "transfer", "contract"]
temperature_list = ["weather", "hot", "cold", "warm"]
#humidity_list = ["humid", "humidity", 'precipitation']
#latitude_list = ["equator", "southern hemisphere", "northern hemisphere"]

print(temperature_list)
