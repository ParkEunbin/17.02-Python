price=float(input("상품가격(만원):"))

if price >=10:
    discount=price*0.2
else:
    discount=price*0.1

final_price=price-discount
print("최종가격: %.2f만원" %final_price)
            
