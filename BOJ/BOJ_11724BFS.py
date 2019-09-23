# 백준 11724번 문제
import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().strip().split())

g = defaultdict(list)

for i in range(M) :
    s_v, e_v = map(int, sys.stdin.readline().strip().split())
    g[s_v].append(e_v)
    g[e_v].append(s_v)

_sum = 0
visited = [] 
for start_v in g :
    if start_v in visited :
        continue
    q = deque([start_v])
    while q :
        p = q.popleft()
        for end_v in g[p] :
            if end_v not in visited :
                q.append(end_v)
                visited.append(end_v)
    _sum += 1
    
for i in range(1, N+1) :
    if i not in visited :
        _sum += 1
print(_sum)