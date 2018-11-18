h=float(input("근무시간:"))
pay=8000

if h>7:
    s=pay*h
    s=s+(pay*(h-7))*0.5
else:
    s=pay*h

print("임금:%.2f원" %s)
