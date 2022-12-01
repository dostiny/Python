# for _ in range(int(input())):
#     H, W, N = map(int, input().split())
#     floor = 0
#     for j in range(1, W + 1):
#         for i in range(1, H + 1):
#             floor = i * 100 + j
#             N -= 1
#             if N == 0:
#                 break
#         if N == 0:
#             break
#     print(floor)

for _ in range(int(input())):
    H, W, N = map(int, input().split())
    h = w = 1
    while True:
        N -= 1
        if N == 0:
            result = h * 100 + w
            break
        else:
            if h == H:
                h = 1
                w += 1
            else:
                h += 1
    print(result)
