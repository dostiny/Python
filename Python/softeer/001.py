import sys

result = 0
for i in range(5):
    S, E = sys.stdin.readline().split()
    SH, SM = map(int, S.split(':'))
    EH, EM = map(int, E.split(':'))
    result += (EH - SH) * 60 + (EM - SM)

print(result)