visited = [0] * 30
for i in range(28):
    n = int(input())
    visited[n - 1] = 1
for j in range(30):
    if visited[j] == 0:
        print(j + 1)