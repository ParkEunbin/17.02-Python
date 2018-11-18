#비행코드,경로출력

code=input("비행코드:")
code=code.upper()

if code.startswith("NYC"):
    print("출발:뉴욕",end="")
else:
    print("잘못입력")

print("<->",end="")

if code.endswith("NRT"):
    print("도착:도쿄")
else:
    print("잘못입력")
