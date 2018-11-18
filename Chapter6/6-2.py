#최댓값 출력
def get_max(n1,n2,n3):
    if n1<n2:
        maxs=n2
    else:
        maxs=n1

    if n3>maxs:
        maxs=n3
    return maxs


print("최댓값",get_max(3,6,8))
