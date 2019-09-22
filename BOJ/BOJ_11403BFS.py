# 백준 11403번 문제
import sys
import copy
from collections import deque

N = int(sys.stdin.readline().strip())

arr = []
for i in range(N) :
    arr.append(list(map(str, sys.stdin.readline().strip().split())))

g = [[] for i in range(len(arr))]

for i in range(len(arr)) :
    for j in range(len(arr[0])) :
        if arr[i][j] == "1" :
            g[i].append(j)

for i in range(len(g)) :
    g_c = copy.deepcopy(g)
    if not g_c[i] :
        continue
    q = deque([i])
    visited = []
    while q :
        v = q.popleft()
        while g_c[v] :
            p = g_c[v].pop()
            if p not in visited :
                q.append(p)
                visited.append(p)

    for val in visited :
        arr[i][val] = "1"

for arr_x in arr :
    print(" ".join(arr_x))