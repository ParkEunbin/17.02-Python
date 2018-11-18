#인사하는 기계

time=int(input("현재시간:"))

if 0<=time<=24:
    if 0<=time<12:
        print("Good Morning")
    elif 12<=time<18:
        print("Good Afternoon")
    else:
        print("Good Evening")
else:
    print("잘못입력")
    
