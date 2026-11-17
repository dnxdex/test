import csv


def read_csv(path):
    reader = open(path, "r")
    headings = next(reader)
    print(f"Headings:\n{headings}")
    print("Values:")
    for line in csv.reader(reader):
        print(line)


read_csv("clothing.csv")
