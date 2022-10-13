def team(li):
    global min_v
    if len(li) == 4:
        # print(li)
        num_v = abs((arr[li[0]][li[1]] + arr[li[1]][li[0]]) - (arr[li[2]][li[3]] + arr[li[3]][li[2]]))
        if min_v > num_v:
            min_v = num_v
        return
    else:
        for i in range(N):
            if i not in li:
                team(li + [i])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
num_li = [i for i in range(N)]
min_v = 0xfffffffffff
team([])
print(min_v)