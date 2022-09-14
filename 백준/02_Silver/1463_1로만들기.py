# N = int(input())
# cnt = 0
# while N != 1:
#     cnt += 1
#     if N % 2 == 0:
#         N = N // 2
#     elif N % 3 == 0:
#         N = N // 3
#     else:
#         N -= 1
# print(cnt)

N = int(input())    # 10
d = [0] * (N + 1)   # 값을 저장할 빈 리스트  # [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]

for i in range(2, N + 1):
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
print(d[N])