N = int(input())
arr = sorted(list(map(int, input().split())))
result = int(input())
cnt, left, right = 0, 0, N - 1
while left != right:
    sum_N = arr[left] + arr[right]
    if sum_N == result:
        cnt += 1
        left += 1
    elif sum_N > result:
        right -= 1
    elif sum_N < result:
        left += 1
print(cnt)