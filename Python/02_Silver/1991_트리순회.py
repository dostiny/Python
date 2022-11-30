N = int(input())
H = [0]
L = [0]
R = [0]

for _ in range(N):
    a, b, c = map(str, input().split())
    H.append(a)
    L.append(b)
    R.append(c)

print(H)
print(L)
print(R)

