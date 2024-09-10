def get_input():
    expression = input("Fraction: ")
    division = False
    for i, char in enumerate(expression):
        if char == "/":
            X=expression[:i]
            Y=expression[i+1:]
            division = True

    if not division:
        return get_input()

    try:
        Y = int(Y)
        X = int(X)
    except ValueError:
        return get_input()

    if X>Y:
        return get_input()
    if Y == 0:
        return get_input()

    return (X,Y)

def toPercent(X,Y):
    percent = round(X/Y*100)
    return percent

def evaluatePercent(percent):
    if(percent<=1):
        return "E"
    elif(percent >=99):
        return "F"
    else:
        return f"{percent}%"


X,Y = get_input()
percent = toPercent(X,Y)
print(evaluatePercent(percent))

