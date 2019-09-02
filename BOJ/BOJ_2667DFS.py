# 백준 알고리즘 2667번 문제 DFS

def DFS(list, count, x, y) :
    list[x][y] = 0

    #좌, 우, 아래, 위
    # 좌
    if y-1 >= 0 :
        if list[x][y-1] == 1 :
            count = DFS(matrix, count+1, x, y-1)
    # 우
    if y+1 < N :
        if list[x][y+1] == 1 :
            count = DFS(matrix, count+1, x, y+1)
    # 아래
    if x+1 < N :
        if list[x+1][y] == 1 :
            count = DFS(matrix, count+1, x+1, y)
    # 위
    if x-1 >= 0 :
        if list[x-1][y] == 1 :
            count = DFS(matrix, count+1, x-1, y)

    return count
    
N = int(input())

matrix = [[int(x) for x in input()] for y in range(N)]

danji = []

for i in range(N) :
    for j in range(N) :
        if matrix[i][j] == 1 :
            danji.append(DFS(matrix, 1, i, j))
            

print(len(danji))

danji.sort()

for i in danji :
    print(i)