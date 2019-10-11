# 백준 1389번 문제
from collections import deque
N, M = map(int, input().split())
G = []
for i in range(M) :
    x, y = map(int, input().split())
    if [x,y] not in G :
        G.append([x,y])
        G.append([y,x])

result = [[0 for _ in range(N)] for __ in range(N)]
for i in range(1, N+1) :
    q = deque([[i,i]])
    visited = [i]
    while q :
        pop_x, pop_y = q.popleft()
        for g_x, g_y in G :
            if g_x == pop_y and g_y not in visited  :
                q.append([g_x, g_y])
                result[i-1][g_y-1] = result[i-1][g_x-1]+1
                visited.append(g_y)
        
_min = M*N
for i in range(N) :
    _sum = sum(result[i])
    if _min > _sum :
        _min = min(_min, _sum)
        number = i+1

print(number)