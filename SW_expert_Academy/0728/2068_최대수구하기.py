T = int(input())

for i in range(1, T+1):
    num_list = list(map(int, input().split()))
    max_num = num_list[0]
    print(f'#{i}', end=' ')
    for j in num_list:
        if max_num <= j:
            max_num = j
    print(max_num)