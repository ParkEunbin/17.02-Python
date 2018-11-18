#최댓값출력
def maxs(numlist):
    maxi=0
    for count in numlist:
        if maxi<count:
            maxi=count
    return maxi


num=[3,6,9,12,15]
print("최댓값:",maxs(num))
