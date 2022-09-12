N, M = map(int, input().split())
num_li = list(map(int, input().split()))

sum_v = 0
max_v = 0
for i in range(N):
    sum_v += num_li[i]
    if sum_v > M:
        sum_v -= num_li[i]
    else:
        max_v = sum_v
print(max_v)