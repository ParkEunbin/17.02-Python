#2와 3의 공배수
list1=[]
list2=[]
a=0

for b in range(30):
    list1.append(b)
    b+=2
for c in list1:
    if c%3==0:
        list2.append(c)
    if len(list2)==10:
        break
print(list1)
print(list2)
