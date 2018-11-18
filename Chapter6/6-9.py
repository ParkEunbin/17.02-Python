#해당원소 위치 찾기
def search(numlist,find):
    for a in range(len(numlist)):
        if numlist[a]==find:
            return a
        
    return -1
            
        

number=[1,3,5,7,9,11,14,16,17,23]
find=int(input("찾을원소:"))
sit=search(number,find)
if sit!=-1:
    print("위치값:",sit)
else:
    print("없음")
