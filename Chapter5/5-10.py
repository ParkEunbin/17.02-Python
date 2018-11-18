#총 열량계산
hamburger={"빵":168,"패티":250, "토마토":20, "양상추":11, "케챱":15, "치즈":60}

print("햄버거재료:", hamburger.keys())


menu=input("재료를 , 로 구분하여 입력:")
total=0

for a in menu.split(","):
    add=hamburger[a]
    total+=add

print("총열량:",total)
