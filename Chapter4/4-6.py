m=[]
i=1

for x in range(5):
    x_list=[]
    for y in range(5):
        x_list.append(i)
        i+=1
    m.append(x_list)

total=0
for x in range(5):
    for y in range(x,5):
        total+=m[x][y]
print("대각선 오른쪽위의 합:",total)

for x in range(5):
    for y in range(0,x+1):
        total+=m[x][y]
print("대각선 아래 합:",total)
        
