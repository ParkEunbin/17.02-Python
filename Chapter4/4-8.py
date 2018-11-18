#표 출력하기
checklist=[]

for a in range(3):
    information=input("이름,점수2개(,로 구분):")
    checklist.append(information.split(","))
    

print("리스트:",checklist)
print(" 학생  시험1  시험2  합계  평균")


for b in range(3):
    total=0
    print("%s"%checklist[b][0], end=" ")
    for c in range(1,3):
        
        print("%d"%int(checklist[b][c]), end=" ")
        total+=int(checklist[b][c])
    average=total/2
    print("%d  %s "%(total,average))
