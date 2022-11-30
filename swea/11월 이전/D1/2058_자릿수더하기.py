# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.

N = int(input())
N_sum = 0

while N >= 10:
    N_sum += N % 10
    N = N // 10
N_sum += N

print(N_sum)