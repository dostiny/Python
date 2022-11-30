N, S = map(int, input().split())
num_li = list(map(int, input().split()))
cnt = 0
def backtrack(k, cur_sum, num):
    global cnt;
    if k == N:
        if sum(pick) == S and len(pick):
            cnt += 1
        pass
    else:
        pick.append(num_li[k])
        backtrack(k + 1, cur_sum + num_li[k], num + 1)
        pick.pop()
        backtrack(k + 1, cur_sum, num)
pick = []
backtrack(0,0,0)
print(cnt)