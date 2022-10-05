def merge_sort(lst):
    global cnt
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    l = merge_sort(lst[:mid])
    r = merge_sort(lst[mid:])

    if l[-1] > r[-1]:
        cnt += 1
    # l, r은 정렬된 리스트
    ret = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            ret.append(l[i])
            i += 1
        else:
            ret.append(r[j])
            j += 1
    if l: ret += l[i:]
    if r: ret += r[j:]

    return ret  # 병합

for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    print(f'#{TC} {merge_sort(arr)[N//2]} {cnt}')