def get_input():
    expression = input("Fraction: ")
    division = False
    for char in expression:
        if char == "/":
            division = True

    if not division:
        return get_input()
    return expression

def toPercent(X,Y):
    percent = round(X/Y*100)
    return percent

def convert(expression):

    for i, char in enumerate(expression):
        if char == "/":
            X=expression[:i]
            Y=expression[i+1:]
    try:
        Y = int(Y)
        X = int(X)
    except ValueError:
        raise ValueError()
    if Y == 0:
        raise ZeroDivisionError()

    if X>Y:
        raise ValueError()


    percent = toPercent(X,Y)
    return percent


def gauge(percent):
    if(percent<=1):
        return "E"
    elif(percent >=99):
        return "F"
    else:
        return f"{percent}%"

def main():
    expression = get_input()
    percent=convert(expression)
    print(gauge(percent))


if __name__ == "__main__":
    main()


