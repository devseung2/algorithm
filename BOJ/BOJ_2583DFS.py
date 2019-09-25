# 백준 2583번 문제
import sys

M, N, K = list(map(int,(sys.stdin.readline().strip().split())))

arr = [[0]*N for i in range(M)]

for i in range(K) :
    start_x, start_y, end_x, end_y = list(map(int,(sys.stdin.readline().strip().split())))

    for i in range(start_y, end_y) :
        for j in range(start_x, end_x) :
            if arr[i][j] != 1 :
                arr[i][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
count_arr = []

for i in range(M) :
    for j in range(N) :
        if arr[i][j] == 0 :
            stack = [[i,j]]
            arr[i][j] = 1
            count = 1
            while stack :
                s_i, s_j = stack[len(stack)-1]
                check = True
                for k in range(4) :
                    temp_x = dx[k] + s_i
                    temp_y = dy[k] + s_j
                    if 0 <= temp_x < M and 0 <= temp_y < N and arr[temp_x][temp_y] == 0 :
                        stack.append([temp_x, temp_y])
                        arr[temp_x][temp_y] = 1
                        count += 1
                        check = False
                        break  
                if check :
                    stack.pop()
            count_arr.append(count)

count_arr.sort()
result = ""
for num in count_arr :
    result += str(num) + " "

print(len(count_arr))
print(result)