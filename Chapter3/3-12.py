#문자열에서 특수문자 제거하기

m=input("문자열을 입력:")
special='''~!@#$%^&*()_+-={}[];':",./<>?'''
new_m=""

index_m=0
while index_m< len(m):
    index_s=0
    while index_s<len(special):
        if m[index_m]==special[index_s]:
            break
        index_s+=1
    else:
        new_m+=m[index_m]
    index_m+=1
print("특수문자 제거 후:%s"%new_m)
