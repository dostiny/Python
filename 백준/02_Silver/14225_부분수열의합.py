# N = int(input())
# arr = list(map(int, input().split()))
# pick = []
# num_li = [0] * 100001
# def backtrack(k, cur_sum): # K: 현재 노드의 높이, 함수 호출 깊이, k번 선택을 한 상태
#     # k번 원소에 대한 선택==> cur_sum에는 0 ~ k-1 원소들에 대한 선택이 계산
#     if k == N:
#         # print(pick, cur_sum)
#         num_li[cur_sum] = 1
#     else:
#         # k번 원소를 포함
#         pick.append(arr[k])
#         backtrack(k + 1, cur_sum + arr[k])
#         pick.pop()
#         # k번 원소를 미포함
#         backtrack(k + 1, cur_sum)
#
# backtrack(0, 0)
# print(num_li.index(0))

# =======================================================

N = int(input())
arr = sorted(list(map(int, input().split())))
num = 1

for i in arr:
    if num < i:
        break
    num += i
    print(num)

print(num)