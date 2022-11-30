import sys; sys.stdin = open('input/12390_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = range(1, 13)
    count = 0
    for i in range(1 << 12):
        li = []
        for j in range(12):
            if i & (1 << j):
                li.append(arr[j])
        if len(li) == N:
            if sum(li) == K:
                count += 1
    print(f'#{test_case} {count}')