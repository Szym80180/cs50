from pyfiglet import Figlet
import pyfiglet as pf
from sys import argv
import random

f = Figlet()
fonts= f.getFonts()

if len(argv)==1:
    font = random.choice(fonts)
elif len(argv)==3:
    if argv[1]=="-f" or argv[1]=="--font":
        if argv[2] in fonts:
            font = argv[2]
        else:
            print("Wrong font")
            sys.exit()
    else:
        print("Wrong arguments")
        sys.exit()
else:
    print("Wrong number of arguments")
    sys.exit()

str = input("Input: ")

f = Figlet(font = font)

print(f.renderText(str))
