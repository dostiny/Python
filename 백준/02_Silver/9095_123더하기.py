num_li = [1, 2, 3]

def num_sum(li):
    global cnt
    if sum(li) == N:
        cnt += 1
    elif sum(li) > N:
        return
    else:
        for i in range(3):
            num_sum(li + [num_li[i]])


for _ in range(int(input())):
    N = int(input())
    cnt = 0
    num_sum([])
    print(cnt)