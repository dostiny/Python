import sys

input = sys.stdin.readline

n = int(input())

stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    print('num = ', num)
    while cur <= num:
        print('cur = ', cur, '+')
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == num:
        print(stack[-1], '-')
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)