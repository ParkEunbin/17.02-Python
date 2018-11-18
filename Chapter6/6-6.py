#잔액출력

def ins(one):
    global won
    won+=one
def out(one):
    global won
    won-=one

def a():
    print("잔액:",won)
    

won=1000
a()
ins(3000)
a()
out(2000)
a()
