#문자열 뒤집기
message=input("문자열 입력:")
length=len(message)
reverse=""

for letter in  range(0, length):
    reverse+= message[length-(letter+1)]

print("반대 문자열:"+reverse)
