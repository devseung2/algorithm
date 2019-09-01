# 백준 알고리즘 1260번 문제
import queue

def DFS(matrix, v, m_list) : 
    m_list.append(v)
    
    for matrix_v in range(1, n+1) :
        if matrix[v][matrix_v] == 1 and m_list.count(matrix_v) == 0 :
            m_list = DFS(matrix, matrix_v, m_list)

    return m_list

def BFS(matrix, v) :
    q = queue.Queue()
    q.put(v)
    q_list = [v]

    while q.qsize() :
        pop_v = q.get()

        for matrix_v in range(1, n+1) :
            if matrix[pop_v][matrix_v] == 1 and q_list.count(matrix_v) == 0 :
                q.put(matrix_v)
                q_list.append(matrix_v)
        
    return q_list


n, m, v = map(int, input().split())

matrix = [[0 for x in range(n+1)] for y in range(n+1)]

for i in range(0, m) :
    start, end = map(int, input().split())
    matrix[start][end] = 1
    matrix[end][start] = 1

m_list = []
print(*DFS(matrix, v, m_list))

print(*BFS(matrix, v))