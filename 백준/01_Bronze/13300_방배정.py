N, K = map(int, input().split())    # 학생수, 방 인원수

sut = [list(map(int, input().split())) for _ in range(N)]
g_cnt = [0] * 6
b_cnt = [0] * 6

for i in range(N):
    if sut[i][0] == 0:
        g_cnt[sut[i][1]-1] += 1
    if sut[i][0] == 1:
        b_cnt[sut[i][1]-1] += 1

result = 0
for y in g_cnt:
    if y == 0:
        pass
    elif y % K == 0:
        result += 1
    elif y < K:
        result += 1
    else:
        result += 2
for x in b_cnt:
    if x == 0:
        pass
    elif x % K == 0:
        result += 1
    elif x < K:
        result += 1
    else:
        result += 2
print(result)