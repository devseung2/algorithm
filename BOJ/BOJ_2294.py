# 백준 2294번 문제

n, k = map(int, input().split())
coin = []
for i in range(n) :
    coin.append(int(input()))

dp = [k+1 for _ in range(k+1)]
dp[0] = 0
for c in coin :
    for j in range(c, k+1) :
        dp[j] = min(dp[j], dp[j-c]+1)
    print(dp)

if dp[k] == k+1 :
    print(-1)
else :
    print(dp[k])