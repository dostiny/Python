N = int(input())
for _ in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.pop(0); b.pop(0)
    ans = ''
    for i in range(4, 0, -1):
        a_cnt = a.count(i)
        b_cnt = b.count(i)
        if a_cnt > b_cnt:
            ans = 'A'
            break
        elif a_cnt < b_cnt:
            ans = 'B'
            break
    else:
        ans = 'D'

    print(ans)