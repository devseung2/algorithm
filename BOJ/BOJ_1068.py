# 백준 1068번 문제
import sys

N = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().strip().split()))
d_node = int(sys.stdin.readline().strip())

arr[d_node] = -2
_sum = 0
q = [arr[d_node]]

while q :
    p = q.pop(0)
    l = arr.count(p)
    for i in range(l) :
        idx = arr.index(p)
        arr[idx] = -2
        q.append(idx)

for i in range(len(arr)) :
    if (arr[i] == -1 and arr.count(i) == 0) or (arr[i] >= 0 and arr[arr[i]] != -2 and arr.count(i) == 0) :
        _sum += 1
print(_sum)