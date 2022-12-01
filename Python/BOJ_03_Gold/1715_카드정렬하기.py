def line(li):
    global min_v
    if len(li) == N:
        cnt = a = 0
        for j in range(N):
            if a == 0:
                a = li[j]
            else:
                a += li[j]
                cnt += a
        if min_v > cnt:
            min_v = cnt
        return
    else:
        for i in range(N):
            if arr[i] not in li:
                line(li + [arr[i]])

N = int(input())
arr = [int(input()) for i in range(N)]
min_v = 0xffffffffffff
line([])

print(min_v)

# ================================================

# N = int(input())
# arr = sorted([int(input()) for i in range(N)])
# result = sum_v = 0
# for j in range(N):
#     if sum_v == 0:
#         sum_v = arr[j]
#     else:
#         sum_v += arr[j]
#         result += sum_v
#
# print(result)