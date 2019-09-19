# 백준 1026번 문제
import sys

N = int(sys.stdin.readline().strip())

A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

A.sort()
S = 0
for a in A :
    max_idx = B.index(max(B))
    S += a * B.pop(max_idx)

print(S)