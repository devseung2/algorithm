# 백준 11052번 문제

N = int(input())
Pi = list(map(int, (input().split())))
dp = [0]
for val in Pi :
    dp.append(val)

for i in range(2, N+1) :
    for j in range(1, i) :
        if i % j == 0 :
            dp[i] = max(dp[i], dp[j]*(i//j))
        else :
            dp[i] = max(dp[i], dp[j]+dp[i%j])
     
print(dp[N])