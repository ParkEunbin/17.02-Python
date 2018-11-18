#국가정렬
nation=[]
for count in range(5):
    nation.append(input("국가입력:"))
    nation.sort()

    for number in range(len(nation)):
        print("%d.%s"%(number+1,nation[number]),end=" ")
        print()
