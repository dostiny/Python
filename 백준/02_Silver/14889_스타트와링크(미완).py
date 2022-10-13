def back(number):
    if len(A) == N//2 or len(B) == N//2:
        pass
    else:
        A.append(number)
        back(number + 1)
        A.pop()
        B.append(number)
        back(number + 1)
        B.pop()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
num_li = [i for i in range(N)]
min_v = 0xfffffffffff
A = [num_li[0]]
B = []
back(1)