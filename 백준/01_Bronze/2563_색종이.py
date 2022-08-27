n = int(input())

paper = [[0]*100 for _ in range(100)]

ans = 0
for rc in range(n):
    x, y = map(int, input().split())
    for r in range(10):
        for c in range(10):
            if paper[y+r][x+c] != 1:
                paper[y+r][x+c] = 1
                ans += 1
print(ans)