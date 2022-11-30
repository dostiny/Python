num = int(input())

for i in range(1, num+1):
    num_list = []
    N = int(input())
    print(f'#{i}', end=' ')
    for j in range(1, N+1):
        if N % j == 0:
            num_list.append(j)
    num_list.sort(reverse=True)
    for x in num_list[0:-1]:
        print(x, end=' ')
    print(num_list[-1])