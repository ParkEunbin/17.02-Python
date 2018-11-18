#평균구하기
def aver(stuple):
    total=0
    for a in stuple:
        total+=a
    average=total/len(stuple)
    return average


score=(30,70,100,40,50)
print("평균:",aver(score))
