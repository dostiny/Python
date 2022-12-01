T = int(input())

for i in range(1, T+1):
    num_list = list(map(int, input().split()))
    sum_num = 0
    how_long = len(num_list)
    print(f'#{i}', end=' ')
    for j in num_list:
        if 0 <= j <= 1000:
            sum_num += j
    print(int(round(sum_num/how_long, 0)))