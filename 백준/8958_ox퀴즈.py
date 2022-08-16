T = int(input())
for _ in range(T):
    oxinput = input()
    cnt = 0
    score = 0
    for i in oxinput:
        if i == 'O':
           cnt += 1
        elif i == 'X':
            cnt = 0

        if cnt != 0:
            score += cnt
    print(score)