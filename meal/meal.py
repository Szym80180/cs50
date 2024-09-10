def main():
    time = input("What time is it? ")
    hours = convert(time)

    if 7<=hours<=8:
        print("breakfast time")
    elif 12<=hours<=13:
        print("lunch time")
    elif 18<=hours<=19:
        print("dinner time")


def convert(time):
    for i, char in enumerate(time):
        if char == ":":
            left =time[:i]
            right = time[i+1:]
    right = float(right)
    left = float(left)
    right = right/60
    result = left+right
    return result



if __name__ == "__main__":
    main()
