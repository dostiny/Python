N = int(input())
arr = [list(input()) for _ in range(N)]
cnt = idx = 0
while idx != N:
    for i in range(idx + 1, N):
        if arr[idx][i] == 'Y':
            cnt += 1
    idx += 1
print(arr)
print(cnt)