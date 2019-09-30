# 백준 7569번 문제
import sys
from collections import deque

M, N, H = list(map(int, sys.stdin.readline().strip().split()))
arr = [[list(map(int,sys.stdin.readline().split())) for i in range(N)] for j in range(H)]
# 뒤, 앞, 왼쪽, 오른쪽, 아래, 위
dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]
dz = [-1,1,0,0,0,0]
q = deque()
tomato = 0
empty = 0
tomato_check = True
for k in range(H) :
    for i in range(N) :
        for j in range(M) :
            if arr[k][i][j] == 1 :
                q.append([k,i,j])
                tomato += 1
            elif arr[k][i][j] == -1 :
                empty += 1
            else :
                tomato_check = False

if tomato_check :
    print(0)
    sys.exit()

_max = 0
while q :
    pop_h, pop_n, pop_m = q.popleft()
    for i in range(6):
        temp_h = pop_h + dz[i]
        temp_n = pop_n + dy[i]
        temp_m = pop_m + dx[i]
        if 0 <= temp_m < M and 0 <= temp_n < N and 0 <= temp_h < H and arr[temp_h][temp_n][temp_m] == 0 :
            arr[temp_h][temp_n][temp_m] = arr[pop_h][pop_n][pop_m] + 1
            _max = max(_max, arr[temp_h][temp_n][temp_m])
            q.append([temp_h, temp_n, temp_m])
            tomato += 1

if tomato != (N*M*H-empty) :
    print(-1)
else :
    print(_max-1)