#이름,비밀번호 입력

name=input("이름입력:")
pw=input("비밀번호 입력:")

for count in range(0,len(pw)-1):
    if pw[count]==pw[count+1]:
        print("연속된 문자가 존재")
        break

else:
    if pw.isalpha() or pw.isdigit():
        print("섞으시오")
    else:
        print("정상처리")
        
