import re
import sys

# src="http://www.youtube.com/embed/xvFZjo5PgG0"

#pattern = r"src=\".+/youtube.com/embed/.+\""
pattern = r"src=\".+/.*youtube.com/embed/.+\""

def main():
    print(parse(input("HTML: ")))


def parse(s):

    match = re.search(pattern, s)
    if not match:
        return "None"
    link = match.group()
    link = link.split('"')[1]
    code = link.split("/")[-1]
    return f"https://youtu.be/{code}"



...


if __name__ == "__main__":
    main()

