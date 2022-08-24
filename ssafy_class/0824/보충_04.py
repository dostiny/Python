name=['A','B','C','D','E']
st=input()  # 출발점 입력
arr=[
    [0,4,0,0,0],
    [0,0,1,2,9],
    [5,0,0,7,0],
    [0,0,0,0,1],
    [0,0,0,0,0],
]
used=[0]*5

Min=int(21e8)
def dfs(now,sum):
    global Min
    if name[now] == 'E':
        # 최소 비용 (최소 sum)
        if Min > sum:
            Min = sum

    for i in range(5):
        if arr[now][i]>0:
            if used[i]==0:
                used[i]=1
                dfs(i,sum+arr[now][i])
                used[i]=0

# 출발점의 인덱스 확인
st_index=0
for i in range(5):
    if name[i]==st:
        st_index=i
        break

used[st_index]=1
dfs(st_index,0)
print(Min)