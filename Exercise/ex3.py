#회원가입기
def check_id(message):
    while True:
        nid=input("아이디입력:")
        if nid.isalpha() or nid.isdigit():
            print("아이디는 문자와 숫자가 같이 포함되어야 합니다.")
            continue
        else:
            break
    return nid
    

def generate_password():
    print("비밀번호는 자동으로 6자리가 생성됩니다")
    import random
    passwd=''
    for a in range(6):
        data=['a','b','c','d','e','f','g','h','i','j'
              ,'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        ins=random.choice(data)
        passwd+=ins
    return passwd
    
def input_addinfo(info1,info2):
    information=[]
    cm=int(input("신장입력:"))
    information.append(cm)
    kg=float(input("몸무게 입력:"))
    information.append(kg)
    return information

def display_member(member):
    for a in member:
        list(a.items())
        for key,item in a.items():
            print(key,":",item)


print("멤버가입")
member=[]

member1={}
message=''
info1=0
info2=0
member1["아이디"]=check_id(message)
    
member1["비밀번호"]=generate_password()
   
member1["추가정보"]=input_addinfo(info1,info2)

member.append(member1)
    
member2={}
message=''
info1=0
info2=0
member2["아이디"]=check_id(message)
    
member2["비밀번호"]=generate_password()
   
member2["추가정보"]=input_addinfo(info1,info2)

member.append(member2)

print(member)

display_member(member)



    
