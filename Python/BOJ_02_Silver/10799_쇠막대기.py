import sys;

arr = list(sys.stdin.readline())
arr.pop()
result = 0
st = []

for i in range(len(arr)):
    if arr[i] == '(':
        st.append('(')
    else:
        if arr[i-1] == '(':
            st.pop()
            result += len(st)
        else:
            st.pop()
            result += 1

print(result)