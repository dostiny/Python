# import sys; sys.stdin = open('input/1859_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    price = list(map(int, input().split()))
    cnt = 0
    money = 0
    for i in range(N-1):
        if price[i] > price[i+1]:
            money += cnt * price[i]
            cnt = 0
        elif price[i] < price[i+1]:
            cnt += 1
            money -= price[i]
        elif price[i] == price[i+1]:
            cnt += 1
            money -= price[i]

        if i == N - 2:
            if price[i] > price[i+1]:
                money += cnt * price[i]
                cnt = 0
            money += cnt * price[N - 1]
            cnt = 0
    print(f'#{tc} {money}')