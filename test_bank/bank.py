def main():
    greeting = input()
    print(f"{value(greeting)}$")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting == "hello":
        return 0
    elif greeting[0]=="h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
