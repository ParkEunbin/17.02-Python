#시험점수 총 합 
def ctotal(name,*score):
    total=0
    for a in score:
        total+=a
    return name,total


print(ctotal("홍길동",100,90,50,70,80))
