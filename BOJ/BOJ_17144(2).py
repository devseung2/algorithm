# 백준 17144번 문제
import sys, copy

R, C, T = list(map(int, sys.stdin.readline().strip().split()))
# 반시계 방향
dr1 = [0,-1,0,1]
dc1 = [1,0,-1,0]
# 시계 방향
dr2 = [0,1,0,-1]
dc2 = [1,0,-1,0]

arr = []
air = []

for i in range(R) : 
    arr.append(list(map(int, sys.stdin.readline().strip().split())))
    for j in range(i, len(arr)) :
        if -1 in arr[j] :
            air.append([j, arr[i].index(-1)])
    
for t in range(T) :
    result = []
    for i in range(R) :
        for j in range(C) :
            if 0 < arr[i][j] :
                val = arr[i][j]//5
                for k in range(4) :
                    temp_r = i + dr1[k]
                    temp_c = j + dc1[k]

                    if 0 <= temp_r < R and 0 <= temp_c < C and arr[temp_r][temp_c] != -1 :
                        result.append([temp_r, temp_c, val])
                        result.append([i,j,-val])

    for i, j, val in result :
        arr[i][j] += val

    for air_i in range(2) :
        stack = [[air[air_i][0], air[air_i][1]+1]]

        for i in range(4) :
            while stack :
                stack_r, stack_c = stack[len(stack)-1]
                
                if air_i == 0 :
                    temp_r = stack_r + dr1[i]
                    temp_c = stack_c + dc1[i]
                else :
                    temp_r = stack_r + dr2[i]
                    temp_c = stack_c + dc2[i]

                if 0 <= temp_r < R and 0 <= temp_c < C and arr[temp_r][temp_c] != -1 :
                    stack.append([temp_r, temp_c])
                else :
                    break
                    
        while stack :
            pop_r, pop_c = stack.pop()
            if len(stack) == 0 :
                arr[pop_r][pop_c] = 0
                break
            arr[pop_r][pop_c] = arr[stack[len(stack)-1][0]][stack[len(stack)-1][1]]

_sum = 0
for i in range(R) : 
    for j in range(C) :
        if 0 < arr[i][j] :
            _sum += arr[i][j]
print(_sum)