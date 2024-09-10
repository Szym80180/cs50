import emoji

code = input("Input: ")

emoji = emoji.emojize(code, language='alias')

print(f"Output: {emoji}")
