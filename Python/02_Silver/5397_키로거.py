for _ in range(int(input())):
    left = []
    right = []
    pwd = input()

    for x in pwd:
        if x == ">":
            if right:
                left.append(right.pop())
        elif x == "<":
            if left:
                right.append(left.pop())
        elif x == "-":
            if left:
                left.pop()
        else:
            left.append(x)

    print("".join(left) + "".join(reversed(right)))
