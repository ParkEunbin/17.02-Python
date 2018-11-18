score=input("점수입력:")

total=0

for a in score.split("-"):
    total+=int(a)

print("총점: %d"%total)
