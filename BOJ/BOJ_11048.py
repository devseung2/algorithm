# 백준 11048번 문제

N, M = map(int, input().split())
arr = [[0 for _ in range(M+1)]]
for i in range(N) :
    arr.append([0]+list(map(int, input().split())))

dp =[[0 for _ in range(M+1)] for __ in range(N+1)]
dp[1][1] = arr[1][1]

for i in range(1, N+1) :
    for j in range(1, M+1) :
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + arr[i][j]

print(dp[N][M])