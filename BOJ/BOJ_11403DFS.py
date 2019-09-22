# 백준 11403번 문제
import sys
import copy

N = int(sys.stdin.readline().strip())

arr = []
for i in range(N) :
    arr.append(list(map(str, sys.stdin.readline().strip().split())))

g = [[] for i in range(N)]
for i in range(N) :
    for j in range(N) :
        if arr[i][j] == "1" :
            g[i].append(j)

for i in range(N) :
    g_c = copy.deepcopy(g)
    if not g_c[i] :
        continue
    stack = [i]
    visited = []
    while stack :
        v = stack[len(stack)-1]
        if g_c[v] :
            p = g_c[v].pop()
            if p not in visited :
                stack.append(p)
                visited.append(p)
        else : 
            stack.pop()
    for val in visited :
        arr[i][val] = "1"

for arr_x in arr :
    print(" ".join(arr_x))