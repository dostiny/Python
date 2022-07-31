orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders_list = orders.split(',')
orders_list.sort(reverse=True)

orders_dict = {}

for order in orders_list:
    if order in orders_dict:
        orders_dict[order] += 1
    else:
        orders_dict[order] = 1

print(orders_dict)