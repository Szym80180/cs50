from csv import DictReader
from sys import argv
import  sys
from tabulate import tabulate

if len(argv)<2:
    print("Too few command line arguments")
    sys.exit(1)

if len(argv)>2:
    print("Too many command line arguments")
    sys.exit(1)

if argv[1][-4:]!=".csv":
    print("Not a csv file")
    sys.exit(1)

rows=[]

with open(argv[1]) as file:
    reader = DictReader(file)
    for row in reader:
        rows.append(row)


print(tabulate(rows, headers="keys", tablefmt="grid"))
