# 백준 알고리즘 2579번 문제

A = int(input())

arr = [0]
for i in range(A) :
    arr.append(int(input()))

dp = [0, arr[1], arr[1]+arr[2], max(arr[1]+arr[3], arr[2]+arr[3])]

for i in range(4, len(arr)) :
    dp.append(max(dp[i-2], dp[i-3]+arr[i-1])+arr[i])

print(dp[A])