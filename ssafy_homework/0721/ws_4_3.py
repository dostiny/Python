input_lst = [1, 1, 3, 3, 0, 1, 1]
lst = []
lst.append(input_lst[0])
for i in range(1, len(input_lst)):
    if input_lst[i] != input_lst[i-1]:
        lst.append(input_lst[i])
print(lst)