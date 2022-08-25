import sys; sys.stdin = open('input/계산기_input.txt', 'r')
# 교수님 풀이
for tc in range(1, 11):
    icp = {'+': 1, '*': 2, '(': 3, ')': 0}
    isp = {'+': 1, '*': 2, '(': 0, ')': 0}
    N = int(input())
    infix = input()
    postfix = ''
    S = []

    for token in infix:
        if token in icp:
            if token == ')':
                while S and S[-1] != '(':
                    postfix += S.pop()
                S.pop()
            else:       # '+', '*', '('
                while S and icp[token] < isp[S[-1]]:
                    postfix += S.pop()
                S.append(token)
        else:
            postfix += token
    while S:
        postfix += token

    for token in postfix:
        if token in icp:
            b = S.pop()
            a = S.pop()
            if token == '+': S.append(a + b)
            else: S.append(a * b)
        else:
            S.append(int(token))
    print(f'#{tc}', S[0])