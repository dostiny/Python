import sys; sys.stdin = open('4831.txt')

# T = int(input())
# for t in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     M_num = list(map(int, input().split()))
#
#     cur = 0  # 현재 정류장번호
#     charge_count = 0  # 충전횟수
#     while cur + K < N:
#         for next in range(cur + K, cur, -1):
#             if next in M_num:
#                 charge_count += 1
#                 cur = next
#                 break
#         else:
#             charge_count = 0
#             break
#
#     print(f'#{t} {charge_count}')

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    # [0] + [1 3 5 7 9] + [10]
    # len(station) = M + 2
    station = [0] + list(map(int, input().split())) + [N]

    cur = 0  # 현재 위치
    cnt = 0  # 충전횟수
    for i in range(1, M + 2):
        # 충전소 사이의 거리를 체크
        if station[i] - station[i - 1] > K:  # 갈수 없음
            cnt = 0
            break
        # 충전할 위치를 결정
        if cur + K < station[i]:
            cur = station[i - 1]
            cnt += 1
    print(f'#{tc} {cnt}')









