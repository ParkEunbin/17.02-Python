def a(m,s):
    count=0
    for b in m:
        if b==s:
            count+=1
        else:
            pass
    return count
        





m=input("문자열 입력:")
s=input("찾을 문자열:")
count=(a(m,s))
print("문자개수:",count)
