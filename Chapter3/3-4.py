#중간글자 출력

word=input("문자열 입력:")
lenth=len(word)

if lenth%2==1:
    word[lenth//2]
    print("중간글자:%s" %letter)
else:
    letter1=word[(lenth//2)-1]
    letter2=word[(lenth//2)]
    print("중간글자: %s"%(letter1+letter2))
