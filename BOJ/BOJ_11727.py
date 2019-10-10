# 백준 11727번 문제
N = int(input())
dp = [0 for _ in range(1000)]
dp[0] = 1
dp[1] = 3
for i in range(2, N) :
    dp[i] = dp[i-2]*2 + dp[i-1]

print(dp[N-1] % 10007)