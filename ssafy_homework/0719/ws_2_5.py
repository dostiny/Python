crops = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
crops_price = []
price = 0
for i in crops:
    crops_price.append(i[1])
    for j in crops_price:
        if price < j:
            price = j
for x in crops:
    if x[1] == price:
        print(x[0])