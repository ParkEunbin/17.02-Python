nchar=0
ndigit=0
nother=0

m=input("문자열입력:")

for letter in m:
    if letter.isalpha():
        nchar+=1
    elif letter.isdigit():
        ndigit+=1
    else:
        nother+=1

print("문자:%d개"%nchar)
print("숫자:%d개"%ndigit)
print("기타:%d개"%nother)
