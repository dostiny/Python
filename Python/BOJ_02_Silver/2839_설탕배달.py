N = int(input())
cnt = 0
result = 0

while N >= 0:
    if N % 5 == 0:          # 5의 배수이면
        cnt += (N // 5)     # 5로 나눈 몫
        result = cnt
        break
    N -= 3
    cnt += 1                # 5의 배수가 될 때까지 설탕 -3, 봉지 +1
else:
    result = -1

print(result)