def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(input):
    vowels = {'a', 'e','i','o','u','A','E','I','O','U'}
    for char in input:
        if char in vowels:
            input = input.replace(char, "")
    return input


if __name__ == "__main__":
    main()
