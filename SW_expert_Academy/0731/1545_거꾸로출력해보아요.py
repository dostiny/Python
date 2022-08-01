int_input = int(input())

num_list = [i for i in range(int_input+1)]
num_list.sort(reverse=True)
for j in num_list:
    print(j, end=' ')
print('')