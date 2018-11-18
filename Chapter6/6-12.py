def cal(op,*su):
    

    if op=='+':
        total=0
        for a in su:
            total+=a
    elif op=='*':
        total=1
        for a in su:
            total*=a
    else:
        print("연산불가")
    return total
    

print("결과",cal('+',1,3,5,7))
print("결과",cal('*',1,3,5,7))
