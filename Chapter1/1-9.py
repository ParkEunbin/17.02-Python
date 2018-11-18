#XOR사용

num1=10
num2=20
temp=num1^num2
num1=temp^num1
num2=temp^num2

print("num1=%d, num2=%d" %(num1,num2))
