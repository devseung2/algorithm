# 백준 알고리즘 9095번 문제

T = int(input())

dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for t in range(T) : 
    N = int(input())
    for n in range(4, N+1) :
        dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
    print(dp[N])