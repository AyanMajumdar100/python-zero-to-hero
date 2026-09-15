import csv

with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    print(reader)        # <_csv.reader object at 0x0000028FFE36DD80>
    print(type(reader))  # <class '_csv.reader'>
    for row in reader:
        print(row)


# EXAMPLE 2: USING DictReader and DictWriter

# DICTREADER: {'name': 'Ayan', 'age': '25', 'role': 'Developer'}
import csv
with open("data.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print(reader)
    for row in reader:
        print(row)  # {'name': 'Ayan', 'age': '25', 'role': 'Developer'}
        print(row["name"], row["age"], row["role"])
        print(row["name"], row["age"], row["role"], row["pass"])
        # Since Pass not present in csv
        # KeyError: 'pass'

# DICTWRITER: turns each row into a dictionary using the header names as keys.
import csv

data = [
    {"name": "Ayan", "age": 25, "role": "Developer"},
    {"name": "Maya", "age": 30, "role": "AI Engineer"}
]
with open("output.csv","w",encoding="utf-8") as file:
    headlines = ['name','age','role']
    writer = csv.DictWriter(file,fieldnames=headlines)
    writer.writeheader()
    writer.writerows(data)

