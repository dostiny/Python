import sys

sys.stdin = open('input/12385_input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    bus = 0
    if K >= arr[1]:
        for i in range(M):
            if bus >= N:
                break
            elif bus == 0:
                bus += K
            elif bus >= arr[i]:
                cnt += 1
                bus += K
            elif arr[i] > bus:
                cnt = 0
                break
    elif arr[1] > K >= arr[0]:
        bus += K
        for j in range(M+1):
            if bus >= N:
                cnt += 1
                break
            if bus == arr[j]:
                bus = j
            elif bus >= arr[j]:
                cnt += 1
                if bus == arr[j+1]:
                    bus = arr[j+1]
                else:
                    bus += K
            elif arr[j] > bus:
                cnt = 0
                break
    print(f'#{test_case} {cnt}')