def back(number):
    global min_v
    if len(A) == N//2 and len(B) == N//2:
        sum_A = sum_B = 0
        for i in A:
            for j in A:
                if i != j:
                    sum_A += arr[i][j]
        for i in B:
            for j in B:
                if i != j:
                    sum_B += arr[i][j]
        if min_v > abs(sum_A - sum_B):
            min_v = abs(sum_A - sum_B)
        return
    else:
        if len(A) != N//2:
            A.append(number)
            back(number + 1)
            A.pop()
        if len(B) != N//2:
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
print(min_v)