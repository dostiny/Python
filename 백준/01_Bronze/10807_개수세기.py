N = int(input())
arr = sorted(list(map(int, input().split())))
result = int(input())
cnt = 0
for i in range(N):
    if arr[i] == result:
        cnt += 1
print(cnt)