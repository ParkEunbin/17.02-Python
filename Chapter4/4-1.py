student=[]
total=0

for count in range(5):
    score=int(input("점수입력:"))
    student.append(score)
    total+=score
average=total/len(student)
print("학생점수:",student)
print("평균:%.1f"%average)
