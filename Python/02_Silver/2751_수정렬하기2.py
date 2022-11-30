import sys;

n = int(sys.stdin.readline())
arr = sorted(list(set([int(sys.stdin.readline()) for _ in range(n)])))
for i in arr:
    print(i)