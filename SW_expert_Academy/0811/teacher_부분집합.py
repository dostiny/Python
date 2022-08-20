# 전체집합 = {1,2,3} N = 3, 모든 부분집합 = 2^n = 8

# bit shift 연산자
arr = [10, 20, 30]
N = len(arr)
for bits in range(1 << N): # 2^N = 8
    print(bits)