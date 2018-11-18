import sys
idnumber=input("주민번호 -없이 입력:")

if "1"<= idnumber[6]<="2":
    year="19"+idnumber[:2]+"년"
elif "3"<=idnumber[6]<="4":
    year="20"+idnumber[:2]+"년"
else:
    print("잘못입력")
    sys.exit()
month=idnumber[2:4]+"월"
day=idnumber[4:6]+"일"


print(year+month+day)
