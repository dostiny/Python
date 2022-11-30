def s(li):
    if len(li) == 3:
        print(li)
        return
    else:
        for i in range(3):
            if i not in li:
                s(li + [i])
s([])