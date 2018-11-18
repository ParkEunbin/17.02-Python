sec=int(input("전체 초 단위의 시간을 입력:"))
h=(sec//60)//60
m=(sec//60)%60
s=sec%60

print("%d초는" %sec, end=" ")
print("%d시간 %d분 %d초 입니다." %(h,m,s))
