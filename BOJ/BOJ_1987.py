# 백준 1987번 문제
R, C = map(int, input().split())
arr = [['' for _ in range(C)] for __ in range(R)]
for i in range(R) :
    _list = list(str(input().strip()))
    for j in range(C) :
        arr[i][j] = _list[j]
visited = [[0 for _ in range(C)] for __ in range(R)]
visited[0][0] = 1
visited_Alpha = [arr[0][0]]
stack = [[0,0]]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
_max = 1

while stack :
    now_r, now_c = stack[len(stack)-1]
    l = len(stack)
    for i in range(visited[now_r][now_c], 4) :
        temp_r = now_r + dr[i]
        temp_c = now_c + dc[i]

        if 0 <= temp_r < R and 0 <= temp_c < C and visited[temp_r][temp_c] == 0 and arr[temp_r][temp_c] not in visited_Alpha :
            stack.append([temp_r, temp_c])
            visited_Alpha.append(arr[temp_r][temp_c])
            visited[now_r][now_c] = i+1
            break

    if l == len(stack) :
        _max = max(_max, len(stack))
        visited[now_r][now_c] = 0
        stack.pop()
        visited_Alpha.pop()
        
print(_max)