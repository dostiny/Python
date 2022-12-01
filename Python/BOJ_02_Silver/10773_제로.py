import sys;

N = int(sys.stdin.readline())
H = []
for _ in range(N):
    i = int(sys.stdin.readline())
    if i != 0:
        H.append(i)
    elif i == 0:
        H.pop()
print(sum(H))
