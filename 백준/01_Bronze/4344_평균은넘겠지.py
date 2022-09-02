for _ in range(int(input())):
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    aver = sum(arr)//n
    cnt = 0
    for i in arr:
        if i > aver:
            cnt += 1
    ans = (format(cnt/n*100, ".3f"))
    print(f'{ans}%')