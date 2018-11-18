#5-10
#비트연산으로 마스킹하기
color=0b1001001110110010
red_mask=0b1111100000000000
green_mask=0b0000011111100000
blue_mask=0b0000000000011111

red=(color&red_mask)>>11
green=(color&green_mask)>>5
blue=color&blue_mask

print("red=%s"%bin(red))
print("green=%s"%bin(green))
print("blue=%s" %bin(blue))
