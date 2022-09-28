import sys;

N = int(sys.stdin.readline())
Nnum = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mnum = list(map(int, sys.stdin.readline().split()))
result = []
for i in Mnum:
    result.append(Nnum.count(i))
print(*result)