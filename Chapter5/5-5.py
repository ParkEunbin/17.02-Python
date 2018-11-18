#개인정보
person={}
person["이름"]='홍길동'
person["성별"]='남'
person["나이"]=20
person["키"]=180

for key in person:
    print("%s:%s" %(key,person[key]))
