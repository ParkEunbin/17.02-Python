fruit={"apple":1500,"banana":1300,"melon":2000}
for a,b in fruit.items():
    print(a,b)
total=0
for c in fruit.keys():
    print("%s의 갯수:"%c, end=" ")
    num=int(input())
    total+=(fruit[c]*num)
print(total,"원")
