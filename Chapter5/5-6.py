#국가코드 검색
nation_code={1:"US",33:"France",44:"Japan"}

print("국가번호:",nation_code)

search=int(input("검색할 번호:"))
if search in nation_code:
    print("국가: %s "%nation_code[search])
else:
    print("추가")
    nation=input("국가입력:")
    nation_code[search]=nation
print(nation_code)
