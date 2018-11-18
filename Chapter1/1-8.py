flag=0b11001100;mask=0b11110000
flag&+mask
print(bin(flag))
flag=0b11001100;mask=0b00001111
flag|=mask
print(bin(flag))
