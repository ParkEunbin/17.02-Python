def a():
    print("##################################")
    print("           s t a r t              ")
    print("##################################")

def b():
    num=int(input("수 입력:"))
    return num

def add(num1,num2):
    c=num1+num2
    return c

def d(re):
    print("결과:",re)
    print("##################################")

a()
num1=b()
num2=b()
re=add(num1,num2)
d(re)
