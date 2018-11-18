#국가이름저장

nation=[]

while True:
    name=input("국가를 입력(종료:exit):")

    if name=="exit":
        break
    if name in nation:
        print("중복된 국가 존재")
        print("다시입력")
        continue
    nation.append(name)
print("국가:",nation)
