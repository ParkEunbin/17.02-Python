#최댓값 출력
a=[]
for i in range(1,6):
    b=input()
    a.append(b)
print (a)

for i in range(len(a)-1):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            temp = a[i]
            a[i]=a[j]
            a[j]=temp



print(a)

