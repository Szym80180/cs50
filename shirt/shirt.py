import PIL
from PIL import Image
from PIL import ImageOps
from sys import argv
import sys

extensions = ["jpg", "jpeg", "png"]

if len(argv)<3:
    print("Too few command line arguments")
    sys.exit(1)

if len(argv)>3:
    print("Too many command line arguments")
    sys.exit(1)

if argv[1].split(".")[1] not in extensions:
    print("Not an accepted file")
    sys.exit(1)

if argv[2].split(".")[1] not in extensions:
    print("Not a accepted file")
    sys.exit(1)

if argv[1].split(".")[1]!=argv[2].split(".")[1]:
    print("Not a accepted file")
    sys.exit(1)

with Image.open("shirt.png")as shirtimg:
    with Image.open(argv[1]) as beforeimg:
        beforeimg = ImageOps.fit(beforeimg, shirtimg.size)
        beforeimg.paste(shirtimg, shirtimg)
        beforeimg.save(argv[2])


