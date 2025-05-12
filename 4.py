def dictionary(lang):
    if lang == "rus":
        for letter in range(1040, 1072):
            yield chr(letter)
    if lang == "eng":
        for letter in range(65, 91):
            yield chr(letter)


print(*dictionary("rus"))
print(*dictionary("eng"))
print('\U0001F44D')
