# =============================================
# ver1
def dfs(start):
    if len(s) == L:
        vowel = 0
        cons = 0
        for j in s:
            if j in vowel_li:
                vowel += 1
            else:
                cons += 1
        if vowel >= 1 and cons >= 2:
            for k in s:
                print(k, end='')
            print()
        return

    for i in range(start, C):
        s.append(arr[i])
        dfs(i + 1)
        s.pop()

L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
vowel_li = ['a', 'e', 'i', 'o', 'u']
s = []
dfs(0)

# =============================================
# ver2
def comb(n, r, start):
    if r == 0:
        coll = vow = 0
        for i in pick:
            if i in vow_li:
                vow += 1
            else:
                coll += 1
        if vow >= 1 and coll >= 2:
            for j in pick:
                print(j, end='')
            print()
        return
    for i in range(start, n - r + 1):
        pick.append(arr[i])
        comb(n, r - 1, i + 1)
        pick.pop()

L, C = map(int, input().split())
arr = sorted(list(input().split()))
pick = []
vow_li = ['a', 'e', 'i', 'o', 'u']
comb(C, L, 0)