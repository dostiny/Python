# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
# print(fact(4))

# =================================

def f(i, N):
    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)

f(0, 3)