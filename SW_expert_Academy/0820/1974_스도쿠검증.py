import sys; sys.stdin = open('input/1974_input.txt', 'r')

for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    # print(arr)
    # 가로
    result1 = 1
    for ar in arr:
        num_arr = []
        for i in range(1, 10):
            for j in ar:
                if i == j:
                    num_arr.append(i)
        if len(num_arr) == 9:
            result1 = 1
        else:
            result1 = 0

    # 세로
    result2 = 0
    for r in range(9):
        num_arr = []
        for i in range(1, 10):
            for c in range(9):
                if i == arr[c][r]:
                    num_arr.append(i)
        if len(num_arr) == 9:
            result2 = 1
        else:
            result2 = 0
    # 3*3
    result3 = 0

    # 결과 곱셈 이기 때문에 하나라도 틀리면 0이 나옴
    result = result1 * result2 * result3
    print(result1 , result2)