for tc in range(1, int(input())+1):
    N, k_min, k_max = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort()
    t1 = min(score)+1
    t2 = t1 + 1
    ans = -1
    while t1 <= (max(score) -1):
        a = b = c = 0 # 초기 반 설정은 0명으로
        for i in range(N):
            if score[i] < t1:
                a += 1
            elif t1 <= score[i] < t2:
                b += 1
            else:
                c += 1
        if k_min <= a <= k_max and k_min <= b <= k_max and k_min <= c <= k_max:
            result = max(a, b, c) - min(a, b, c)
            if ans == -1:
                ans = result

            elif ans > result:
                ans = result

        if (t2 + 1) >= max(score):
            t1 += 1
            t2 = t1 + 1
            continue
        t2 += 1

    print(f'#{tc}', ans)