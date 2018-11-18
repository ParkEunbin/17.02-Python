money=int(input("교환할 금액 입력:"))
m500=money//500
money%=500
m100=money//100
money%=100
m50=money//50
money%=50
m10=money//10
money%=10
print("500원 %d개, 100원 %d개, 50원 %d개, 10원 %d개" %(m500,m100,m50,m10))
