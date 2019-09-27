# 백준 2193번 문제
import sys

N = int(sys.stdin.readline().strip())
dp = [1,1] 
for i in range(2, N) :
    dp.append(dp[i-2]+dp[i-1])
print(dp[N-1])