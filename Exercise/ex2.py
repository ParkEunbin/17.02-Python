#최종본

me=input("수 or '짝'을 입력:")
if me=='1':
    com=2
    while True:

        if com%3==0:
          
            print("computer:짝")
            
        
            if com%10==0:
                answer=input("그만하시겠습니까?(y/n)")
                if answer.lower() =='y':
                    break
                else:
                    pass
                    
            me=input("수 or '짝'을 입력:")

            if me!='짝' and int(me)!=(com+1):
                print("당신이 졌습니다.")
                break
            elif me!='짝' and int(me)%3==0:
                print("당신이 졌습니다.")
                break
            elif me=='짝' and (com+1)%3!=0:
                print("당신이 졌습니다.")
                break
            elif me=='짝':
                pass
            else:
                pass
        
            
            
        elif com%3!=0:

            
            print("computer:%d"%com)
            
            if com%10==0:
                answer=input("그만하시겠습니까?(y/n)")
                if answer.lower() =='y':
                    break
                else:
                    pass

            me=input("수 or '짝'을 입력:")
            
            
            if me!='짝' and int(me)!=(com+1):
                print("당신이 졌습니다.")
                break
            elif me!='짝' and int(me)%3==0:
                print("당신이 졌습니다.")
                break
            elif me=='짝' and (com+1)%3!=0:
                print("당신이 졌습니다.")
                break
            elif me=='짝':
                pass
            else:
                pass
       
        com+=2
        
