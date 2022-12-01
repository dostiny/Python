N = int(input())
paper = [[0]*1001 for _ in range(1001)]
ans = 0
for k in range(N):
    c, r, x, y = map(int, input().split())
    for j in range(y):
        for i in range(x):
            if 0 <= c+x <= 1000 and 0 <= r+y <= 1000:
                paper[r+y][c+x] = k+1
for i in paper:
    print(i)