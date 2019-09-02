# 백준 알고리즘 2667번 문제 BFS
import queue

def BFS(list, count, x, y) :
    list[x][y] = 0

    q = queue.Queue()
    q.put((x,y))

    while q.qsize() > 0 :
        q_x, q_y = q.get()

        # #좌, 우, 아래, 위
        # 좌
        if q_y-1 >= 0 :
            if list[q_x][q_y-1] == 1 :
                q.put((q_x,q_y-1))
                list[q_x][q_y-1] = 0
                count += 1

        # 우
        if q_y+1 < N :
            if list[q_x][q_y+1] == 1 :
                q.put((q_x,q_y+1))
                list[q_x][q_y+1] = 0
                count += 1

        # 아래
        if q_x+1 < N :
            if list[q_x+1][q_y] == 1 :
                q.put((q_x+1,q_y))
                list[q_x+1][q_y] = 0
                count += 1

        # 위
        if q_x-1 >= 0 :
            if list[q_x-1][q_y] == 1 :
                q.put((q_x-1,q_y))
                list[q_x-1][q_y] = 0
                count += 1

    return count

N = int(input())

matrix = [[int(x) for x in input()] for y in range(N)]

danji = []

for i in range(N) :
    for j in range(N) :
        if matrix[i][j] == 1 :
            danji.append(BFS(matrix, 1, i, j))

print(len(danji))

danji.sort()

for i in danji :
    print(i)