items = {}

while(True):
    try:
        item = input().upper()
    except EOFError:
        break
    else:
        if item in items:
            items[item]+=1
        else:
            items[item]=1

itemList = list(items.keys())

itemList.sort()

for item in itemList:
    print(f"{items[item]} {item}")
