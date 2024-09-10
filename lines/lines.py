from sys import argv
import sys

c=0

if len(argv)<2:
    print("Too few command line arguments")
    sys.exit(1)

if len(argv)>2:
    print("Too many command line arguments")
    sys.exit(1)

if argv[1][-3:]!=".py":
    print("Not a Python file")
    sys.exit(1)

try:
    with open(argv[1]) as file:
        for line in file:
            line = line.strip()
            if line:
                if line[0] != '#':
                    c+=1
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)

print(c)
