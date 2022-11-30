import sys; sys.stdin = open('input/글자수_input.txt', 'r')

for tc in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    max_c = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if max_c < cnt:
            max_c = cnt
    print(f'#{tc} {max_c}')