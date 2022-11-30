T = int(input())

for i in range(T):
    input_num = list(map(int, input().split()))
    print(f'#{i+1}')
    a, b = input_num[0], input_num[1]
    num_list = [j for j in range(1, a*b+1)]
    for x in range(1, a+1):
        for y in num_list[x-1::a]:
            print(y, end=' ')
        print('')