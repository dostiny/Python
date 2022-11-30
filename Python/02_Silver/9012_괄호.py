import sys;
N = int(sys.stdin.readline())

result = 0
for _ in range(N):
    arr = list(sys.stdin.readline())
    arr.pop()
    n = len(arr)
    if n % 2:
        result = -1
    else:
        cnt = 0
        while len(arr) != 0:
            a = arr.pop()
            if a == ')':
                cnt += 1
            elif a == '(':
                cnt -= 1
            if cnt < 0:
                result = -1
                break
        if cnt == 0:
            result = 1
        elif cnt:
            result = -1
    if result == 1:
        print('YES')
    elif result == -1:
        print('NO')