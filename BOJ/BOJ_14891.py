# 백준 14891번 문제
from collections import deque

wheel = deque([] for _ in range(4))
for i in range(4) :
    for _list in list(map(str, input().split())) :
        for v in _list :
            wheel[i].append(int(v))

K = int(input())
for i in range(K) :
    num, direction = map(int, input().split())
    direction_info = [0,0,0,0]
    direction_info[num-1] = direction
    # 오른쪽 톱니바퀴
    for j in range(num, 4) :
        if wheel[j][6] == wheel[j-1][2] :
            break
        direction_info[j] = direction_info[j-1]*(-1)
    # 왼쪽 톱니바퀴
    for j in range(num-2, -1, -1) :
        if wheel[j][2] == wheel[j+1][6] :
            break
        direction_info[j] = direction_info[j+1]*(-1)

    for j in range(4) :
        if direction_info[j] == 1 :
            pop = wheel[j].pop()
            wheel[j].insert(0,pop)
        elif direction_info[j] == -1 :
            pop = wheel[j].pop(0)
            wheel[j].append(pop)

_sum = 0
for i in range(4) :
    _sum += wheel[i][0]*(2**i)
print(_sum)