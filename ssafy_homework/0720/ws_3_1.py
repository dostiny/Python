fruit = "apple", 'rottenBanana', 'apple', 'RoTTenorange', 'Orange'
fruit = [i.lower() for i in fruit]
fruit_list = []

for i in fruit:
    if i[:6] == 'rotten':
        fruit_list.append(i[6:])
    else:
        fruit_list.append(i)

print(fruit_list)