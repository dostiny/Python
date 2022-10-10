from sys import stdin

S = stdin.readline

S_data = S().strip()

def solv():
    stack = []

    cnt = 0
    before = ''
    for c in S_data:
        if c == '(':
            stack.append([cnt - 1, before])
            cnt = 0
        elif c == ')':
            info = stack.pop()
            cnt = cnt*info[1] + info[0]
        else:
            cnt += 1
            before = int(c)
    print(cnt)
solv()