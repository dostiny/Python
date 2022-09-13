N = int(input())
cnt = 0
while N != 1:
    cnt += 1
    if N % 2 == 0:
        N = N // 2
    elif N % 3 == 0:
        N = N // 3
    else:
        N -= 1
print(cnt)