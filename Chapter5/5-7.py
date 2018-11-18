#수도출력
city={"한국":"서울","일본":"도쿄","미국":"워싱턴"}

while True:
    nation=input("국가:")
    if nation=='종료':
        break

    result=city.get(nation)
    if result:
        print("수도:%s"%result)
    else:
        print("국가없음")
        
