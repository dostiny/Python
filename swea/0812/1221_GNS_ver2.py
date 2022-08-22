import sys; sys.stdin = open('input/1221_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    K, N = map(str, input().split())
    N = int(N)
    arr = list(map(str, input().split()))
    num_arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    new_arr = []
    for i in num_arr:
        for j in arr:
            if i == j:
                new_arr += [i]
    print(K)
    print(*new_arr)
