K, N = map(int, input().split())
arr = list(int(input()) for _ in range(K))
start, end = 1, max(arr)

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for line in arr:
        cnt += line // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)