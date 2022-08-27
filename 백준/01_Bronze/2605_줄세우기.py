n = int(input())
order = list(map(int, input().split()))

line = []
for i in range(n):
    line.insert(i-order[i], i+1)

for j in line:
    print(j, end=' ')