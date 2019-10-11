# 백준 10026번 문제
N = int(input())
arr = [list(str(input())) for i in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
part = [1,1]
for n in range(2) :
    visited = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if visited[i][j] != 0 :
                continue
            stack = [[i,j]]
            color = [arr[i][j]]
            if n == 1 and arr[i][j] == "R" or n == 1 and arr[i][j] == "G":
                color = ["R","G"]
            
            while stack :
                s_i, s_j = stack[len(stack)-1]
                l = len(stack)
                for k in range(4) :
                    temp_i = s_i + dx[k]
                    temp_j = s_j + dy[k]

                    if 0 <= temp_i < N and 0 <= temp_j < N and visited[temp_i][temp_j] == 0 and arr[temp_i][temp_j] in color :
                        stack.append([temp_i,temp_j])
                        visited[temp_i][temp_j] = part[n]
                        break

                if l == len(stack) :
                    stack.pop()
            part[n] += 1

print(part[0]-1, part[1]-1)