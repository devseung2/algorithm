# 백준 1697번 문제
import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().strip().split()))
q = deque([N])
count = 0
dx = [-1, 1, 2]
visited = [0] * 100001
visited[N] = 1

if N > K :
    print(N-K)
elif N == K :
    print(0)
else : 
    idx = 1
    while q :
        q_count = 0
        if K in q :
            break
        for i in range(idx) :
            pop_num = q.popleft()
            for i in range(3) :
                result = 0
                if i < 2 :
                    result = pop_num + dx[i]
                else :
                    result = pop_num * dx[i]
                    
                if 0 <= result <= 100000 and visited[result] == 0 :
                    visited[result] = 1
                    q.append(result)
                    q_count += 1
        count += 1
        idx = q_count
    print(count)