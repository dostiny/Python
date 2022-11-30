import sys; sys.stdin = open('input/12396_input.txt', 'r')

for test_case in range(1, int(input())+1):
    str1 = input()
    N = len(str1)
    str_li = [0 for _ in range(N)]
    top = -1
    for i in str1:
        if i == '(' or i == '{':
            top += 1
            str_li[top] = i
        elif i == ')' or i == '}':
            if top < -1:
                break
            top += 1
            str_li[top] = i
            if str_li[top-1] == '(' and str_li[top] == ')':
                top -= 2
            elif str_li[top-1] == '{' and str_li[top] == '}':
                top -= 2
    if top == -1:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')