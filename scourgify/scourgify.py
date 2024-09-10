import csv
import sys
from sys import argv



if len(argv)<3:
    print("Too few command line arguments")
    sys.exit(1)

if len(argv)>3:
    print("Too many command line arguments")
    sys.exit(1)

if argv[1][-4:]!=".csv":
    print("Not a csv file")
    sys.exit(1)

if argv[2][-4:]!=".csv":
    print("Not a csv file")
    sys.exit(1)

students=[]

with open(argv[1]) as file:
    reader = csv.DictReader(file)
    for line in reader:
        students.append(line)

with open(argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first","last","house"])
    csv.writer(file).writerow(["first","last","house"])
    for student in students:
        name = student["name"]
        last, first = name.split(", ")
        writer.writerow({"first": first,"last": last,"house": student["house"]})






