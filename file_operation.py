import csv
csv_data=[
    ["name","age","city"]
    ["ram","36","butwal"]
    ["hari","15","palpa"]
]
with open("villian.csv","w") as file:
    writer=csv.writer(file)
    writer.writerows(csv_data)
    print(writer)