import sys; sys.stdin = open('input/GNS_input.txt', 'r')

for tc in range(1, int(input())+1):
    T, N = input().split()
    arr = list(map(str, input().split()))
    li = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    new_li = []
    for i in li:
        for j in arr:
            if i == j:
                new_li.append(i)
    print(f'#{tc}', *new_li)