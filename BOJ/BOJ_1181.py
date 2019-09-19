# 백준 1181번 문제
import sys

N = int(sys.stdin.readline())

h = {}
for i in range(N) : 
    _in = sys.stdin.readline().strip()
    h[_in] = len(_in)

arr = sorted(h.items(),key= lambda x : x[0])
arr.sort(key = lambda x : x[1])

for key, val in arr :
    print(key)