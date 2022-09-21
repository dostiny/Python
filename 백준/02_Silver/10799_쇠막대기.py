import sys;

arr = list(sys.stdin.readline())
arr.pop()
answer = 0
st = []

for i in range(len(arr)):
    if arr[i] == '(':
        st.append('(')
    else:
        if arr[i-1] == '(':
            st.pop()
            answer += len(st)
        else:
            st.pop()
            answer += 1

print(answer)