def binggo():
    for i in numcnt:
        cnt = 1
        ans = 0
        for r in range(5):
            for c in range(5):
                if player1[r][c] == i:
                    player1[r][c] = 0
                if player1[r][c] == 0:
                    for rr in range(5):
                        sum_v = 0
                        for cc in range(5):
                            sum_v += player1[rr][cc]
                        if sum_v == 0:
                            ans += 1
                            if ans == 3:
                                return cnt
                        sum_v = 0
                        for cc in range(5):
                            sum_v += player1[cc][rr]
                        if sum_v == 0:
                            ans += 1
                            if ans == 3:
                                return cnt
                        sum_v = 0
                        for cc in range(5):
                            sum_v += player1[cc][cc]
                        if sum_v == 0:
                            ans += 1
                            if ans == 3:
                                return cnt
                        sum_v = 0
                        for cc in range(5):
                            sum_v += player1[4-cc][cc]
                        if sum_v == 0:
                            ans += 1
                            if ans == 3:
                                return cnt
                    else:
                        break
        cnt += 1


player1 = [list(map(int, input().split())) for _ in range(5)]
arr = [list(map(int, input().split())) for _ in range(5)]
numcnt = []
for ar in arr:
    for a in ar:
        numcnt += [a]

print(binggo())
