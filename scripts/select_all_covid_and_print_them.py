import pandas as pd

metadata_csv = pd.read_csv("../metadata.csv")

i = 0
for row in metadata_csv.iloc:
    if row["finding"] != "COVID-19":
        continue
    i += 1
    print(f'''{row['folder']}/{row['filename']}''')
print(i)
