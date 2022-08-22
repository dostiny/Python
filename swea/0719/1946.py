for i in range(1,int(input())+1):
    temp = ""
    for j in range(int(input())):
        N, K = map(str, input().split(" "))
        temp += N * int(K)
    
    n = 0
    print("#%d" % i)
    while n < len(temp):
        print(temp[0+n:10+n])
        n += 10