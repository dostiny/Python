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