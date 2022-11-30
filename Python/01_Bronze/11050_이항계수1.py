def factorial(num):
    result = 1
    for i in range(2, num+1):
        result *= i
    return result

n, k = map(int, input().split())

print(factorial(n) // (factorial(n-k) * factorial(k)))