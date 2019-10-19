# 백준 2573번 문제
import copy
from collections import deque

N, M = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arr = [[0 for _ in range(M)] for __ in range(N)]
bingsan = []
for i in range(N) :
    _list = list(map(int, input().split()))
    for j in range(M) :
        arr[i][j] = _list[j]
        if arr[i][j] != 0 :
            bingsan.append([i,j])

count = 0
while True :
    if len(bingsan) == 0 :
        count = 0
        break

    visited = [[0 for _ in range(M)] for __ in range(N)]
    visited[bingsan[0][0]][bingsan[0][1]] = -1
    visited_count = 1
    bingsan_check = deque([bingsan[0]])
    minus_bingsan = []
    while bingsan_check :
        x, y = bingsan_check.popleft()
        zero_count = 0

        for i in range(4) :
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if arr[temp_x][temp_y] != 0 and visited[temp_x][temp_y] != -1 :
                visited[temp_x][temp_y] = -1
                bingsan_check.append([temp_x,temp_y])
                visited_count += 1
            if arr[temp_x][temp_y] == 0 :
                zero_count += 1
        minus_bingsan.append([x,y,zero_count])

    if len(bingsan) != visited_count :
        break

    for i in range(len(minus_bingsan)) :
        x, y, zero = minus_bingsan[i]
        arr[x][y] -= zero
        if arr[x][y] <= 0 :
            arr[x][y] = 0
            bingsan.pop(bingsan.index([x,y]))

    count += 1

print(count)