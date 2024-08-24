import csv
csv_data=[
    ["name","class","age"],
    ["ram","12","18"],
    ["sita","10","16"]
]
with open("villian.csv","w") as file:
    writer=csv.writer(file)
    writer.writerows(csv_data)
    