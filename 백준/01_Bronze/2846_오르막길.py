N = int(input())
arr = list(map(int, input().split()))
temp = 0
ans = []

for i in range(1, N):
    if arr[i] > arr[i - 1]:
        temp += arr[i] - arr[i - 1]
        if i == N - 1:
            ans.append(temp)
    else:
        ans.append(temp)
        temp = 0

print(max(ans))
