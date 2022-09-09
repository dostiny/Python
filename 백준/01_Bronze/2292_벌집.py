N = int(input())

ans = 0
# if N == 1:        # 이부분을 추가했을때 런타임 에러 뜸 왜그런지 모르겠음
#     ans = 1
# else:
cnt = 1
p = 1
while True:
    if N == 1:
        break
    p += 6 * cnt
    if N <= p:
        cnt += 1
        break
    cnt += 1

print(cnt)

# 1, 2~7, 8~19, 20~37, ...
# 1, 6, 12, 18, 24, ...
# 1, 6*1, 6*2, 6*3, 6*4, ...