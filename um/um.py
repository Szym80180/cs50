import re
import sys

pattern = r"\bum\b"

def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    count = len(re.findall(pattern, s))
    return count




if __name__ == "__main__":
    main()
