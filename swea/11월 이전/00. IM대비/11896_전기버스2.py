def backtrack(index, gas, cnt):
    global result
    gas -= 1
    if index >= (N - 1):
        if result >= cnt:
            result = cnt
        return
    if result <= cnt:
        return
    backtrack(index + 1, bustop[index], cnt + 1)
    if gas:
        backtrack(index + 1, gas, cnt)

for TC in range(1, int(input()) + 1):
    N, *bustop = list(map(int, input().split()))
    result = 0xfff
    backtrack(1, bustop[0], 0)
    print(f'#{TC} {result}')