message=input("문자열 입력:")
word=""
for letter in message:
    if letter == " ":
        print(word)
        word=""
        continue
    word+=letter
print(word)
