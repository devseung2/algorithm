# 백준 알고리즘 1463 번 문제

X = int(input())

dp = [0, 0, 1, 1]

for i in range(4, X+1) :
    dp.append(dp[i-1] + 1)

    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[int(i/3)] + 1)
    elif i % 2 == 0 :
        dp[i] = min(dp[i], dp[int(i/2)] + 1)

print(dp[X])