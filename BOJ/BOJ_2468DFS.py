# 백준 2468번 문제

import sys, copy

N = int(sys.stdin.readline().strip())

arr = []
_max = 0
for i in range(N) :
    _list = list(map(int, sys.stdin.readline().strip().split()))
    if max(_list) > _max :
        _max = max(_list)
    arr.append(_list)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = N*N
count_max = 0

for k in range(0, _max+1) :   
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] <= k :
                arr[i][j] = 0
    count = 0   
    copy_arr = copy.deepcopy(arr)
    for i in range(N) :
        for j in range(N) :
            if copy_arr[i][j] == 0 :
                continue
            stack = [[i,j]]
            copy_arr[i][j] = 0
            count += 1
            while stack :
                s_x, s_y = stack[len(stack)-1]
                check = True
                for z in range(4) :
                    temp_x = dx[z] + s_x
                    temp_y = dy[z] + s_y    
                    if 0 <= temp_x < N and 0 <= temp_y < N and copy_arr[temp_x][temp_y] > k :
                        copy_arr[temp_x][temp_y] = 0
                        stack.append([temp_x, temp_y])
                        check = False
                        break
                if check :
                    stack.pop()
    count_max = max(count_max, count)
print(count_max)