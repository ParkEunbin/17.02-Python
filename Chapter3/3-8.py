#다이아몬드모양 별찍기
width= int(input("다이아몬드 폭입력(홀수):"))
star="*"
loop=width-(width//2)

if width%2==1:
    for count in range(loop):
        print(star.center(width))
        star+="**"
    for count in range(loop-1,0,-1):
        star="*"*(count*2-1)
        print(star.center(width))
else:
    print("홀수입력하시오")
