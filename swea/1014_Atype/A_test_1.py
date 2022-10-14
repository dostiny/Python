import sys; sys.stdin = open('input_1.txt')

for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = sorted(list(map(int, input().split())), reverse=True)
    day = 0
    while len(set(arr)) != 1:
        day += 1
        top = arr[0]
        if day % 2 == 1:            # 홀수
            for i in range(1, N):
                if top - arr[i] == 1:
                    arr[i] += 1
                    break
                elif top - arr[i] == 2:
                    pass
                elif top - arr[i] >= 3:
                    arr[i] += 1
                    break
        elif day % 2 == 0:          # 짝수
            for j in range(1, N):
                if top - arr[j] == 1:
                    pass
                elif top - arr[j] == 2:
                    arr[j] += 2
                    break
                elif top - arr[j] >= 3:
                    arr[j] += 2
                    break

    print(f'#{TC}', day)