T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt = 0
    max_c = 0
    for i in str1:
        for j in str2:
            if i == j:
                cnt += 1
        if max_c < cnt:
            max_c = cnt
        cnt = 0
    print(f'#{test_case} {max_c}')