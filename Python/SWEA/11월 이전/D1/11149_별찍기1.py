num = int(input())

for i in range(1, num+1):
    star = int(input())
    print(f'#{i}')
    for j in range(1, star+1):
        print('*' * j)