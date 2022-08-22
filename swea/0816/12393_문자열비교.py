T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')

# for test_case in range(1, T+1):
#     str1 = input()
#     str2 = input()
#     sl1, sl2 = len(str1), len(str2)
#     cnt = 0
#     for i in range(sl2):
#         if str2[i] == str1[0]:
#             for j in range(sl1)
#                 if

