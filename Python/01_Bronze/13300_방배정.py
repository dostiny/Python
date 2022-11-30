N, K = map(int, input().split())    # 학생수, 방 인원수

girl = [0] * 6
boy = [0] * 6

for _ in range(N):
    S, H = map(int, input().split())
    if S == 0:
        girl[H-1] += 1
    elif S == 1:
        boy[H-1] += 1

result = 0
for i in range(6):
    if girl[i] % K == 0:
        result += girl[i] // K
    elif girl[i] % K != 0:
        result += girl[i] // K + 1
    if boy[i] % K == 0:
        result += boy[i] // K
    elif boy[i] % K != 0:
        result += boy[i] // K + 1
print(result)