import sys; sys.stdin = open('12395_input.txt', 'r')

for tc in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    cnt = [0] * 128
    for ch in str2:
        cnt[ord(ch)] += 1

    ans = 0
    for ch in str1:
        val = cnt[ord(ch)]
        if ans < val:
            ans = val
    print(f'#{tc} {ans}')