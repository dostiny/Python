# for TC in range(1, int(input()) + 1):
#     N = int(input())
#     arr = sorted(list(map(int, input().split())))
#     n = N//2
#     result = []
#     for i in range(5):
#         result.append(arr[N - 1 - i])
#         result.append(arr[i])
#     print(f'#{TC}', *result)

#ver2
for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result  = []
    idx = -2
    while len(result) < 10:
        max_v, min_v = 0, 101
        for i in range(N):
            if idx == -2:
                if max_v < arr[i]:
                    max_v = arr[i]
                if min_v > arr[i]:
                    min_v = arr[i]
            else:
                if max_v < arr[i] and result[idx] > arr[i]:
                    max_v = arr[i]
                if min_v > arr[i] and result[idx + 1] < arr[i]:
                    min_v = arr[i]
        result += [max_v, min_v]
        idx += 2
    print(f'#{TC}', *result)