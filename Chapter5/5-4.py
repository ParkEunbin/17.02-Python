#총점구하기
student={"학생1":95,"학생2":83,"학생3":80}

total=0
for name in student:
    total+=student[name]
print(total)
