from sys import stdin

N = int(stdin.readline())
Nnum = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
Mnum = list(map(int, stdin.readline().split()))

num_dic = {}

for i in Nnum:
    if i in num_dic:
        num_dic[i] += 1
    else:
        num_dic[i] = 1

for j in Mnum:
    if j in num_dic:
        print(num_dic[j], end=' ')
    else:
        print(0, end=' ')