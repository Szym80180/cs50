input = input("Input: ")
vowels = {'a', 'e','i','o','u','A','E','I','O','U'}

for char in input:
    if char in vowels:
        input = input.replace(char, "")

print(input)
