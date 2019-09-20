# 백준 1100번 문제
import sys

arr = []

for i in range(8) :
    arr.append(sys.stdin.readline().strip())

_sum = 0 
for i in range(8) :
    for j in range(8) :
        if i % 2 == 0 and j % 2 == 0 and arr[i][j] == 'F' or i % 2 == 1 and j % 2 == 1 and arr[i][j] == 'F' :
                _sum += 1
print(_sum)