import sys; sys.stdin = open('input/괄호검사_input.txt', 'r')

# for test_case in range(1, int(input())+1):
#     str1 = input()
#     N = len(str1)
#     str_li = [0 for _ in range(N)]
#     top = -1
#     for i in str1:
#         if i == '(' or i == '{':
#             top += 1
#             str_li[top] = i
#         elif i == ')' or i == '}':
#             if top < -1:
#                 break
#             top += 1
#             str_li[top] = i
#             if str_li[top-1] == '(' and str_li[top] == ')':
#                 top -= 2
#             elif str_li[top-1] == '{' and str_li[top] == '}':
#                 top -= 2
#             else:
#                 break
#     if top == -1:
#         print(f'#{test_case} {1}')
#     else:
#         print(f'#{test_case} {0}')

for tc in range(1, int(input())+1):
    st = input()
    n = len(st)
    top = -1
    st_li = [0] * n
    for i in st:
        if i == '{' or i == '(':
            top += 1
            st_li[top] = i
        elif i == '}' or i == ')':
            top += 1
            if i == '}' and st_li[top-1] == '{':
                top -= 2
            elif i == ')' and st_li[top-1] == '(':
                top -= 2
    if top == -1:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)