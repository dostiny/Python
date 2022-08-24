# import sys; sys.stdin = open("4837.txt", "r")

arr = [10, 20, 30]
bits = [0, 0, 0]

for i in range(2):
    bits[0] = i
    for j in range(2):
        bits[1] = j
        for k in range(2):
            bits[2] = k
            print(bits, end=' ')
            for l in range(3):
                if bits[l]: print(arr[l], end=' ')
            print()

# bit shift 연산자
arr = [10, 20, 30]
N = len(arr)

for bits in range(1 << N): # 2^N = 8
    for i in range(N): # i => 0, 1, 2
        if bits & (1 << i):
            print(arr[i], end=' ')

    print()






