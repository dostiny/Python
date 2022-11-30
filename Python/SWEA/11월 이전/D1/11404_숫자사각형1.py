T = int(input())
 
for i in range(1, T+1):
    hw_list = []
    H, W = map(int, input().split())
    print(f'#{i}')
    for x in range(1, H*W+1):
        hw_list.append(x)
    for x in range(H):
        for y in range(W):
            print(hw_list[y], end=' ')
        print('')
        hw_list = hw_list[W:]