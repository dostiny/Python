# import sys; sys.stdin = open('input/1859_input.txt', 'r')
# 1
# 5
# 6426 9445 8772 81 3447
# 10
# 629 3497 7202 7775 4325 3982 4784 8417 2156 1932

for tc in range(1, int(input())+1):
    N = int(input())
    price = list(map(int, input().split()))
    max_v = 0
    money = 0
    for i in range(N-1, -1, -1):
        if max_v < price[i]:
            max_v = price[i]
        else:
            money += max_v
            money -= price[i]
    print(f'#{tc} {money}')