T = int(input())
 
for i in range(1, T+1):
    num_list = list(map(int, input().split()))
    sum_num = 0
    print(f'#{i}', end=' ')
    for j in num_list:
        if j % 2:
            sum_num += j
    print(sum_num)