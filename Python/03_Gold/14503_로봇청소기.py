N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
clean = 0
visited = [[0] * M for _ in range(N)]
# 현재 위치를 청소한다.
visited[r][c] =1
clean += 1
# 1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# 2. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# 3. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# 4. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
while True:
    check = 0                       # 청소기 위치 이동할 때 마다 초기화
    for _ in range(4):              # 4방향 확인
        d = (d + 3) % 4             # 반시계방향으로 회전하려면
        nr, nc = r + dy[d], c + dx[d]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited[nr][nc] == 0:   # 청소할수 있을때
            visited[nr][nc] = 1
            clean += 1
            r, c = nr, nc
            check = 1
            break                       # 청소를 했다면 처음으로 돌아가기

    if check == 0:                      # 4방향 확인했는데 청소가 되어있을 때
        br, bc = r - dy[d], c - dx[d]   # 뒤로가기
        if arr[br][bc] == 1:            # 다 청소를 한 경우
            print(clean)
            break
        else:                           # 청소할 곳이 남았을 때
            r, c = br, bc

