def ctotal(name,*score):
    total=0
    for a in score:
        total+=a
    return name,total


print(ctotal("박은빈",100,90,50,70,80))
