message=input("문자열을 입력:")
nchar=0
ndigit=0
nother=0
for letter in message:
    if 'A'<=letter or 'a'<=letter:
        nchar=nchar+1
    elif '0'<=letter<='9':
        ndigit=ndigit+1
    else:
        nother=nother+1

print("문자:%d개" %nchar)
print("숫자:%d개" %ndigit)
print("기타:%d개" %nother)
