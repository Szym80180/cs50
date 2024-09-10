def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string

def main():
    x = input()
    text = convert(x)
    print(text)


main()
