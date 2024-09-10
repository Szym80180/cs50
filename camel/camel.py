name = input ("camelCase: ")

for char in name:
    if char.isupper():
        name = name[:name.find(char)] +"_" + name[name.find(char):]



name = name.lower()
print(name)


