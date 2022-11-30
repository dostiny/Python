N, M = map(int, input().split())
num_li = list(map(int, input().split()))

sum_v = 0
max_v = 0
for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            sum_v = num_li[i] + num_li[j] + num_li[k]
            if max_v < sum_v <= M:
                max_v = sum_v
print(max_v)
