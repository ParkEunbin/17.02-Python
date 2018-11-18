#국가코드
nation_code={1:"US",33:"France",44:"Japan"}

print(nation_code)

search=int(input("삭제할 번호:"))
if search in nation_code:
    print("삭제국가:%s"%nation_code.pop(search))
else:
    priint("번호 없음")
