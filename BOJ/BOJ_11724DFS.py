# 백준 11724번 문제
import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().strip().split())

g = defaultdict(list)
for i in range(M) :
    s_v, e_v = map(int, sys.stdin.readline().strip().split())
    g[s_v].append(e_v)
    g[e_v].append(s_v)

_sum = 0
visited = [] 
for v in range(1, N+1) :
    if v in visited :
        continue
    stack = [v]
    while stack :
        start_v = stack[len(stack)-1]
        if g[start_v] :
            end_v = g[start_v].pop()
            if end_v not in visited :
                stack.append(end_v)
                visited.append(end_v)
        else :
            stack.pop()
    _sum += 1

print(_sum)