#사칙연산기

def cal(num1,num2):
    a=num1+num2
    b=num1-num2
    c=num1*num2
    d=num1/num2
    return a,b,c,d


num1=int(input("첫번째 수:"))
num2=int(input("두번째 수:"))
result=cal(num1,num2)
print("덧셈:%d"%result[0])
print("뺄셈:%d"%result[1])
print("곱셈:%d"%result[2])
print("나눗셈:%.2f"%result[3])
