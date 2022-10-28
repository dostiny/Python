from collections import deque

for _ in range(int(input())):
    st = list(input())
    N = int(input())
    S = input().rstrip()[1:-1].split(",")
    arr = deque()
    for i in S:
        if i.isdigit():
            arr.append(i)

    flag = 0
    reversepoint = 0
    if st.count('D') > N:
        flag = 1
    elif  N == 0:
        if st.count('D') == 0:
            pass
        elif st.count('D') != 0:
            flag = 1
    else:
        for j in st:
            if j == 'R':
                reversepoint += 1
            elif j == 'D':
                if reversepoint % 2 == 0:
                    arr.popleft()
                elif reversepoint % 2 == 1:
                    arr.pop()
        if reversepoint % 2 == 0:
            pass
            # print(f'[{",".join(arr)}]')
        elif reversepoint % 2 == 1:
            arr.reverse()
            # print(f'[{",".join(arr)}]')
    if flag == 0:
        print(f'[{",".join(arr)}]')
    elif flag == 1:
        print('error')

    # if st.count('D') > N:
    #     print('error')
    # elif  N == 0:
    #     if st.count('D') == 0:
    #         print('[]')
    #     elif st.count('D') != 0:
    #         print('error')
    # else:
    #     for j in st:
    #         if j == 'R':
    #             reversepoint += 1
    #         elif j == 'D':
    #             if reversepoint % 2 == 0:
    #                 arr.popleft()
    #             elif reversepoint % 2 == 1:
    #                 arr.pop()
    #     if reversepoint % 2 == 0:
    #         print(f'[{",".join(arr)}]')
    #     elif reversepoint % 2 == 1:
    #         arr.reverse()
    #         print(f'[{",".join(arr)}]')
    #     else:
    #         print('error')

'''
4
RDD
4
[1,2,3,4]
DR
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
'''