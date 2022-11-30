import sys; sys.stdin = open('input/제로_input.txt', 'r')

# 그냥 내장함수 사용해서 푼것
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     n_li = []
#     for i in arr:
#         if i != 0:
#             n_li.append(i)
#         elif i == 0:
#             n_li.pop()
#     sum_v = 0
#     for j in n_li:
#         sum_v += j
#     print(f'#{tc} {sum_v}')


# 스택 사용 하려고 한것
for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    new_li = [0]*N
    top = -1

    for i in arr:
        if i != 0:
            top += 1
            new_li[top] = i
        elif i == 0:
            new_li[top] = 0
            top -= 1

    sum_v = 0
    for j in new_li:
        sum_v += j

    print(f'#{tc} {sum_v}')