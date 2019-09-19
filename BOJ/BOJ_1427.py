# 백준 1427번 문제
import sys

N = sys.stdin.readline().strip()

arr = []
for i in range(len(N)) :
    arr.append(N[i:i+1])

arr.sort(reverse=True)
result = ""
for val in arr :
    result += str(val)

print(result)