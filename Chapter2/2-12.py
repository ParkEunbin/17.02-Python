#비밀번호 확인

passwd = "990627"
idcard = 1

while idcard<=5:
    answer=input("비밀번호 6자리 입력:")      
    if answer==passwd:
            print("일치")
            break
    else:
        print("비밀번호가 일치하지 않습니다.남은기회:%d번"%(5-idcard))
    idcard+=1
else:
    print("끝")
