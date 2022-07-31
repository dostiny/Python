T = int(input())
hw_list = []

for i in range(1, T+2):
    input_list = list(map(int, input().split()))
    H = input_list[0]
    W = input_list[1]
    print(f'#{i}')
    for x in range(1, H*W+1):
        hw_list.append(x)
    for x in range(1, H*W+1):
        for y in range(W):
            print(hw_list[y], end=' ')
        print('')
        hw_list = hw_list[W:]
