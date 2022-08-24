# 인접행렬

name = list(input().split())    # A B C D E F
arr = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

answer = []
def dfs(now):
    global answer
    answer.append((name[now]))

    for i in range(6):
        if arr[now][i] == 1:
            dfs(i)

dfs(0)  # 탐색을 시작하는 'A' 0번 인덱스
print(*answer)