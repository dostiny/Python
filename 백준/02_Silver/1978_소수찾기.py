n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in arr:
    cnt = 0
    if i == 1:
        pass
    else:
        for j in range(2, i+1):
            if i % j == 0:
                cnt += 1
            if cnt == 2:
                break
        if cnt == 1:
            result += 1
print(result)