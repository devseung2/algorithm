# 백준 1021번 문제
from collections import deque

N, M = map(int, input().split())
_list = deque([1+i for i in range(N)])
seq = deque(list(map(int, input().split())))
count = 0
while seq :
    idx = _list.index(seq[0]) 
    # 오른쪽 이동
    if idx > len(_list)//2 :
        for i in range(len(_list)-idx) :
            pop_n = _list.pop()
            _list.appendleft(pop_n)
            count += 1
    # 왼쪽 이동
    else :
        for i in range(idx) :
            pop_n = _list.popleft()
            _list.append(pop_n)
            count += 1

    _list.popleft()
    seq.popleft()
print(count)