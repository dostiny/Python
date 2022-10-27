for _ in range(int(input())):
    st = list(input())
    N = int(input())
    S = input()
    arr = []
    for i in S:
        if i.isdigit():
            arr.append(i)

    reversepoint = 0
    if st.count('D') > N or N == 0:
        print('error')
    else:
        for j in st:
            if j == 'R':
                reversepoint += 1
            elif j == 'D':
                if reversepoint % 2 == 0:
                    arr.pop(0)
                elif reversepoint % 2 == 1:
                    arr.pop()
        if reversepoint % 2 == 0:
            print(f'[{",".join(arr)}]')
        elif reversepoint % 2 == 1:
            arr.reverse()
            print(f'[{",".join(arr)}]')
        else:
            print('error')