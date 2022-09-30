# from collections import deque
#
# # BFS 메서드 정의
# def bfs(graph, start, visited):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드를 방문 처리
#     visited[start] = True
#     # 큐가 빌 때까지 반복
#     while queue:
#         # 큐에서 하나의 원소를 뽑아 출력하기
#         v = queue.popleft()
#         print(v, end=' ')
#         # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# # 각 노드가 연결된 정보를 표현 (2차원 리스트)
# graph = [[],
#          [2, 3, 8],
#          [1, 7],
#          [1, 4, 5],
#          [3, 5],
#          [3, 4],
#          [7],
#          [2, 6, 8],
#          [1, 7],
#     ]
#
# # 각 노드가 방문된 정보를 표현 (1차원 리스트)
# visited = [0] * 9
#
# # 정의된 DFS 함수 호출
# bfs(graph, 1, visited)

N = 5
arr = [i  for i in range(N)]
# 4번의 선택을 통해 하나의 case
# tree 의 높이, 함수 호출 깊이
# 선택지 2가지 ( 함수 호출 횟수 ) ==> 선택 저장 ==> 경로

cnt = 0
def backtrack(k, cur_sum, num):
    # k: 현재 노드 높이, 함수 호출 깊이, K번의 선택을 한 상태
    # k번 원소에 대한 선택 ==> cur_sum 에는 0 ~ k -1 원소들에 대한 선택이 계산
    if k == N:
        global cnt; cnt += 1
        print(pick)
        pass
    else:
        # 첫번째 선택 => 저장, 계산작업
        # k번 원소 포함
        pick.append(arr[k])
        backtrack(k + 1, cur_sum + arr[k], num + 1)
        pick.pop()
        # 초기상태로 돌아와서, 두번째 선택
        # k번 원소 미포함
        backtrack(k + 1, cur_sum, num)
pick = []
backtrack(0,0,0)