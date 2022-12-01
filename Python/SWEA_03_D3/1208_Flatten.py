for TC in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    max_i, min_i = 0, 0
    max_v, min_v = 0, 999999999
    while N != 0:
        for i in range(len(arr)):
            if arr[max_i] < arr[i]:
                max_i = i
            if arr[min_i] > arr[i]:
                min_i = i
        arr[max_i] -= 1
        arr[min_i] += 1
        N -= 1
    for j in arr:
        if max_v < j:
            max_v = j
        if min_v > j:
            min_v = j
    print(f'#{TC}', max_v - min_v)