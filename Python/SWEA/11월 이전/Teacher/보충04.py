arr = [[3, 5, 4], [1, 1, 2], [1, 3, 9]]
y, x = map(int,input().split()) # 1 1

directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
sum = 0

for i in range(4):
    dy = y + directy[i]
    dx = x + directx[i]
    if dy < 0 or dy > 2 or dx < 0 or dx >2: continue
    sum += arr[dy][dx]
print(sum)
