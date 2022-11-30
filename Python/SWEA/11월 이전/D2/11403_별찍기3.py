num = int(input())

for i in range(1, num+1):
    input_list = list(map(int, input().split()))
    N = input_list[0]
    M = input_list[1]
    if 1 <= N <= 10 and 1<= M <= 3:
        print(f'#{i}')
        if M == 1:
            for j in range(1, N+1):
                print('*' * j)
        elif M == 2:
            for x in range(N, 0, -1):
                print('*' * x)
        elif M == 3:
            for a in range(1, N*2, 2):
                print(f'{"*" * a:^5}')
    else:
        break
