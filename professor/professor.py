import random


def answer_handler(sum,x,y):
    #print("6 + 6 =")
    for i in range(3):
        try:
            answer = int(input(f"{x} + {y} ="))
        except ValueError:
            print("EEE")
            continue

        if answer == sum:
            return 1
        else:
            print("EEE")
    print(f"{x} + {y} = {sum}")
    return 0

def main():
    points = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x+y
        points+=answer_handler(sum,x,y)
    print(points)




def get_level():
    while True:
        try:
            level = int(input())
        except ValueError:
            continue
        else:
            break
    levels = [1,2,3]
    if level not in levels:
        return get_level()
    else:
        return level




def generate_integer(level):
    if level == 1:
        bottom = 0
        range = 10
    elif level == 2:
        bottom = 10
        range = 100
    elif level == 3:
        bottom = 100
        range = 1000

    number = random.randrange(bottom, range)
    return number



if __name__ == "__main__":
    main()
