num_input = int(input())

num_list = []
for i in range(1, num_input+1):
    if num_input % i == 0:
        print(i, end=' ')
print(' ')