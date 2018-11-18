names=[]
name_str=input("5명이름을 차례로 입력:")
names=name_str.split()
search=input("삭제 할 이름:")
if search in names:
    names.remove(search)
    print("%s가 삭제 되었습니다."%search)
else:
    print("존재하지 않습니다.")

print("이름리스트")
for count in range(len(names)):
    print("%d.%s"%(count+1,names[count]),end=" ")
