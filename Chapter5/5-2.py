person=[]

for count in range(2):
    student={}
    student["학번"]=int(input("학번:"))
    student["이름"]=input("이름:")
    student["전공"]=input("전공:")
    person.append(student)

print(person)
