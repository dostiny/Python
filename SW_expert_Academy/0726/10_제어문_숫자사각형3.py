T = int(input())
 
for i in range(1, T+1):
    H, W = map(int, input().split())
    print(f'#{i}')
    hw_list = [x for x in range(1, H*W+1)]
    for x in range(H):
        a = hw_list[:W]
        if x % 2:
            a.sort(reverse=True)
        for k in a:
            print(k, end=' ')
        print('')
        hw_list = hw_list[W:]