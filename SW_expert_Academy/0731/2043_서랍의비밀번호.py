P, K = map(int, input().split())

count_num = 1
for i in range(1000):
    if P == K:
        print(count_num)
        break
    else:
        K += 1
        count_num += 1