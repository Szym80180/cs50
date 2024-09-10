due = 50
accepted = [25,10,5]

while due >0:
    print(f"Amount Due: {due}")
    amount = int(input("Insert Coin: "))
    if amount in accepted:
        due -= amount
        if due <=0:
            break
    else:
        continue


due = abs(due)
print(f"Change Owed: {due}")
