N = int(input())
tree = list(map(int, input().split()))
d = list(map(int, input()))

for i in range(N):
    if tree[i] in d:
        d.append(i)
        tree[i] = -1
print(tree)

print(len(set(tree)) - 1)


# ==================================
