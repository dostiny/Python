fruit = 'apple,rottenBanana,apple,RoTTenorange,Orange'
rotten_list = fruit.lower().split(',')
fruit_list = []

for fru in rotten_list:
    if fru[:6] == 'rotten':
        fruit_list.append(fru[6:])
    else:
        fruit_list.append(fru)
print(fruit_list)