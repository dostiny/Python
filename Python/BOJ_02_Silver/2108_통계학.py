import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# 산술평균 - 다 더해서 / n
print(round(sum(arr) / n))

# 중앙값
arr.sort()
print(arr[n // 2])

# 최빈값 - 빈출
cnt_li = Counter(arr).most_common()
if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1]:  # 최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])

# 최댓값-최솟값
print(max(arr) - min(arr))