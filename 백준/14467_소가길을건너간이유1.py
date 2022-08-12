T = int(input())

dic_cow = {}
cnt = 0
cow, water = map(int, input().split())
dic_cow[cow] = water
for test_case in range(1, T):
    cow, water = map(int, input().split())
    if dic_cow[cow] == water:
        dic_cow[cow] = water
    else:
        cnt += 1
        dic_cow[cow] = water
print(cnt)