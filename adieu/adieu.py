from sys import exit
names = []

while True:
    try:
        name =input("Name: ")
    except EOFError:
        break
    names.append(name)

str = "Adieu, adieu, to "

if len(names)==1:
    str += names[0]
    print(str)
    exit()
if len(names)==2:
    str += f"{names[0]} and {names[1]}"
    print(str)
    exit()

for i in range(len(names)-1):
    str+=f"{names[i]}, "

str+=f"and {names[len(names)-1]}"

print(str)
