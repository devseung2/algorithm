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
            l = len(visited)
            _x = visited[l-1][0]
            _y = visited[l-1][1]
            # 위
            if [_x, _y-1] in arr :
                _y -= 1
            # 오른쪽
            elif [_x+1, _y] in arr :
                _x += +1
            # 아래
            elif [_x, _y+1] in arr :
                _y += 1
            # 왼쪽
            elif [_x-1, _y] in arr :
                _x -= 1
            # back tracking
            else :
                visited.pop()
                continue

            # 이동한 경우
            visited.append([_x, _y])
            arr.pop(arr.index([_x, _y]))
        _sum += 1
    print(_sum)