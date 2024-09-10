def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if(CorrectLength(s) and StartsWithLetters(s) and s.isalnum() and CorrectNumbers(s)):
        return True
    else:
        return False

def CorrectLength(plate):
    if 2<=len(plate)<=6:
        return True
    else:
        #print("corlen")
        return False

def StartsWithLetters(plate):
    if(plate[0].isdigit() or plate[1].isdigit()):
        #print("strt")
        return False
    else:
        return True

def CorrectNumbers(s):
    numbers = False
    for char in s:
        if not numbers and char=="0":
            return False

        if char.isdigit():
            numbers=True
        else: #nie jest numerem
            if numbers: #były numery
                return False
            else: #nie było jeszcze numerów to wszystko git
                continue
    return True




main()
