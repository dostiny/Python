for _ in range(1, int(input()) + 1):
    TC, N = map(str, input().split())
    arr = list(map(str, input().split()))
    numst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    numli = [0] * 10
    for i in arr:
        if i == 'ZRO':
            numli[0] += 1
        elif i == 'ONE':
            numli[1] += 1
        elif i == 'TWO':
            numli[2] += 1
        elif i == 'THR':
            numli[3] += 1
        elif i == 'FOR':
            numli[4] += 1
        elif i == 'FIV':
            numli[5] += 1
        elif i == 'SIX':
            numli[6] += 1
        elif i == 'SVN':
            numli[7] += 1
        elif i == 'EGT':
            numli[8] += 1
        elif i == 'NIN':
            numli[9] += 1
    print(TC)
    for j in range(10):
        for _ in range(numli[j]):
            print(numst[j], end=' ')
    print()