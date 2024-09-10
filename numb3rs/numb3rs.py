import re
import sys

pattern = r"(^\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.match(pattern, ip)
    if not match:
        return False
    for i in range(1,5):
        if int(match.group(i))>255 or int(match.group(i))<0:
            return False
    return True



...


if __name__ == "__main__":
    main()
