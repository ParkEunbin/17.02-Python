#최대최소값 구하기
def max_min(ntuple):
    maxs=0
    for a in ntuple:
        if a>maxs:
            maxs=a
    mins=10
    for a in ntuple:
        if a<mins:
            mins=a
    return maxs,mins



num=(2,3,5,7,8,9)
maxs,mins=max_min(num)
print("최대:",maxs)
print("최소:",mins)
