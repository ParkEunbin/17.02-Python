#체형 판단기

kg=float(input("몸무게(kg):"))
m=float(input("키(m):"))
bmi=kg/m**2

print("당신의 bmi값은 %.2f입니다."%bmi)

while 1:
    if bmi<18.5:
        print("마른체형")
    elif 18.5<= bmi<25:
        print("표준체형")
    elif 25<= bmi<30:
        print("비만체형")
    else :
        print("고도비만")

    answer=input("계속하시겠습니까?(y/n)")

    if answer==n:
        break
