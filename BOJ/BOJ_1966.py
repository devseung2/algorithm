# 백준 1966번 문제
from collections import deque
T = int(input())
for i in range(T) :
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    while q :
        q_pop = q.popleft()
        if len(q) == 0 or M == 0 and max(q) <= q_pop :
            break
        elif max(q) > q_pop :
            q.append(q_pop)
        if M == 0 :
            M = len(q)
        M -= 1
    print(N-len(q))