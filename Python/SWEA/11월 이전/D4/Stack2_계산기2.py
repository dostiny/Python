import sys; sys.stdin = open('input_계산기2.txt')

for TC in range(1, 11):
    N = int(input())
    arr = input()
    stack = [int(arr[0])]
    i = 1
    while i < N:
        if arr[i] == '*':
            stack[-1] = stack[-1] * int(arr[i + 1])
        else:
            stack.append(int(arr[i + 1]))
        i += 2
    print(f'#{TC} {sum(stack)}')



# for TC in range(1, 11):
#     n = int(input())
#     w = input()
#     stack = [int(w[0])]
#     i = 0
#     while i != n - 1:
#         if w[i + 1] == '*':
#             stack[-1] = stack[-1] * int(w[i + 2])
#         else:
#             stack.append(int(w[i + 2]))
#         i += 2
#     print(f'#{TC} {sum(stack)}')