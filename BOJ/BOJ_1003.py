# 백준 알고리즘 1003번 문제

T = int(input())

dp = [[0]*2 for i in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]

for i in range(T) : 
    N = int(input())

    for j in range(2, N+1) :
        dp[j] = [dp[j-2][0] + dp[j-1][0], dp[j-2][1] + dp[j-1][1]]

    print(dp[N][0], dp[N][1])