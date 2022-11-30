# import sys; sys.stdin = open('input/IM_Magnetic_input.txt', 'r')
'''
7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 1 2 2
0 0 0 0 0 1 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2
'''

# for tc in range(1, 11):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     for c in range(N):
#         nc, sc, ns_li = 0, 0, []
#         for r in range(N):
#             if arr[r][c] == 1:
#                 nc += 1
#                 ns_li.append(arr[r][c])
#             elif arr[r][c] == 2:
#                 sc += 1
#                 ns_li.append(arr[r][c])
#
#         if nc == 0 or sc == 0:
#             for r in range(N):
#                 arr[r][c] = 0
#         else:
#             for ma in ns_li:
#                 pass

for tc in range(1):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    # 1은 N 2는 S     N극은 위 S 극은 아래
    ans = 0
    for c in range(N):
        cnt = 0
        for r in range(N):
            if table[r][c] == 1 and cnt != 1:
                cnt = 1
            elif table[r][c] == 2 and cnt == 1:
                ans += 1
                cnt = 0
    print(f'#{tc}',ans)