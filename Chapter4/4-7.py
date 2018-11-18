#합격불합격 판정
checklist=[]
name=input("선수입력:")
checklist.append(name)
score=input("1,2차 점수를 ,로 구분하여 입력:")
checklist.append(score.split(","))
print("판정리스트",checklist)

average=(float(checklist[1][0])+float(checklist[1][1]))/2
if average>=8.0:
    result="합격"
else:
    result="불합격"

print("이름",name,"평균:",average,"판정:",result)
