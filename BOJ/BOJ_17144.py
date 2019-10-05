# 백준 17144번 문제
import sys, copy

R, C, T = list(map(int, sys.stdin.readline().strip().split()))
dr1 = [0,-1,0,1]
dc1 = [1,0,-1,0]
dr2 = [0,1,0,-1]
dc2 = [1,0,-1,0]
arr = []

for i in range(R) :
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

air = []
for i in range(R) :
    if -1 in arr[i] :
        air.append([i, arr[i].index(-1)])

for t in range(T) :
    result = copy.deepcopy(arr)
    visited = [[0 for i in range(C)] for j in range(R)]
    for i in range(R) :
        for j in range(C) :
            if 0 < arr[i][j] :
                val = (arr[i][j]//5)
                for k in range(4) :
                    temp_r = i + dr1[k]
                    temp_c = j + dc1[k]

                    if 0 <= temp_r < R and 0 <= temp_c < C and arr[temp_r][temp_c] != -1 :
                        result[temp_r][temp_c] += val
                        result[i][j] -= val

    arr = copy.deepcopy(result)
    for air_i in range(2) :
        stack = [[air[air_i][0], air[air_i][1]+1]]

        while stack :
            stack_r, stack_c = stack[len(stack)-1]
            if (air_i == 0 and arr[stack_r+1][stack_c] == -1) or (air_i == 1 and arr[stack_r-1][stack_c] == -1) :
                break
                
            for i in range(4) :
                temp_r = 0
                temp_c = 0
                if stack_c == air[air_i][1] :
                    if air_i == 0 :
                        temp_r = stack_r + dr1[3]
                        temp_c = stack_c + dc1[3]
                    else :
                        temp_r = stack_r + dr2[3]
                        temp_c = stack_c + dc2[3]
                else :
                    if air_i == 0 :
                        temp_r = stack_r + dr1[i]
                        temp_c = stack_c + dc1[i]
                    else :
                        temp_r = stack_r + dr2[i]
                        temp_c = stack_c + dc2[i]

                if 0 <= temp_r < R and 0 <= temp_c < C and visited[temp_r][temp_c] == 0 :
                    stack.append([temp_r, temp_c])
                    visited[temp_r][temp_c] = 1
                    break
        while stack :
            pop_r, pop_c = stack.pop()
            if len(stack) == 0 :
                arr[pop_r][pop_c] = 0
                break
            arr[pop_r][pop_c] = result[stack[len(stack)-1][0]][stack[len(stack)-1][1]]

_sum = 0
for i in range(R) : 
    for j in range(C) :
        if 0 < arr[i][j] :
            _sum += arr[i][j]
print(_sum)