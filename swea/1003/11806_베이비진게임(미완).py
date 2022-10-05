for TC in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    play1 = []
    play2 = []
    idx = 0
    ans = 0
    bp = 0
    while idx != 12:
        play1.append(arr[idx])
        play2.append(arr[idx + 1])
        play1.sort(); play2.sort()
        np = len(play1)
        if np >= 3:

            # if play1[np - 3] == play1[np - 2] == play1[np - 1]:
            #     ans = 1
            #     break
            # elif play1[np - 3] == play1[np - 2] + 1 == play1[np - 1] + 2:
            #     ans = 1
            #     break
            # if play2[np - 3] == play2[np - 2] == play2[np - 1]:
            #     ans = 2
            #     break
            # elif play2[np - 3] == play2[np - 2] + 1 == play2[np - 1] + 2:
            #     ans = 2
            #     break
            for i in range(0, np - 2):
                for j in range(1, np - 1):
                    for k in range(2, np):
                        if play1[i] == play1[j] == play1[k]:
                            ans = 1
                        elif play1[i] + 1 == play1[j] and play1[i] + 2 == play1[k]:
                            ans = 1
                        if ans:
                            break

                        if play2[i] == play2[j] == play2[k]:
                            ans = 2
                        elif play2[i] + 1 == play2[j] and play2[i] + 2 == play2[k]:
                            ans = 2
                        if ans:
                            break
                    if ans:
                        break
                if ans:
                    break
            if ans:
                break
        idx += 2

    print(ans)