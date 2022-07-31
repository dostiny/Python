num = int(input())

for i in range(1, num+1):
    num_list = list(map(int, input().split()))
    print(f'#{i} {len(num_list)} {num_list[-1]}')