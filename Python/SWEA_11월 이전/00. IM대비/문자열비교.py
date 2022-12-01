import sys; sys.stdin = open('input/문자비교_input.txt', 'r')

for tc in range(1, int(input())+1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))
    l_st1, l_st2 = len(str1), len(str2)
    n = l_st2 - l_st1 + 1
    result = 0
    i = j = cnt = 0
    while True:
        if str2[i] == str1[j]:
            i += 1
            j += 1
            cnt += 1
        elif str2[i] != str1[j]:
            i += 1
            j = 0
            cnt = 0

        if cnt == l_st1:
            result = 1
            break
        elif i == l_st2:
            result = 0
            break
    print(f'#{tc} {result}')