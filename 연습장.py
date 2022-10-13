def s(li):
    if len(li) == 4:
        print(li)
        return
    else:
        for i in range(4):
            if i not in li:
                s(li + [i])
s([])