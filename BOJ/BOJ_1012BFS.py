# 백준 1012번 문제
import sys

T = int(sys.stdin.readline().strip())

for i in range(T) :
    M, N, K = map(int, sys.stdin.readline().strip().split())
    arr = []
    for j in range(K) :
        x,y = map(int, sys.stdin.readline().strip().split())
        arr.append([x,y])

    _sum = 0 
    while arr :
        visited = [arr.pop(0)]
        while visited :
            p = visited.pop(0)
            _x = p[0]
            _y = p[1]
            # 위
            if [_x, _y-1] in arr :
                visited.append([_x, _y-1])
                arr.pop(arr.index([_x, _y-1]))
            # 오른쪽
            if [_x+1, _y] in arr :
                visited.append([_x+1, _y])
                arr.pop(arr.index([_x+1, _y]))
            # 아래
            if [_x, _y+1] in arr :
                visited.append([_x, _y+1])
                arr.pop(arr.index([_x, _y+1]))
            # 왼쪽
            if [_x-1, _y] in arr :
                visited.append([_x-1, _y])
                arr.pop(arr.index([_x-1, _y]))
            
        _sum += 1
    print(_sum)