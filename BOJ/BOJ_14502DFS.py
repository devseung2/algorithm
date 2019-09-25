# 백준 14502번 문제
import sys
import copy
from itertools import combinations
from collections import deque

arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
empty = []
virus = []
_max = 0

N, M = map(int, sys.stdin.readline().strip().split())

for i in range(N) :
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

def addVirus(copy_arr) : 
    stack = copy.deepcopy(virus)
    while stack :
        p_x, p_y = stack[len(stack)-1]
        check = True
        for i in range(4) :
            temp_x = p_x + dx[i]
            temp_y = p_y + dy[i]
            if 0 <= temp_x < N and 0 <= temp_y < M and copy_arr[temp_x][temp_y] == 0 :
                copy_arr[temp_x][temp_y] = 2
                stack.append([temp_x,temp_y])
                check = False
                break
        if check :
            stack.pop()
    return copy_arr
    
def checkVirus(copy_arr) : 
    count = 0
    for i in range(N) : 
        for j in range(M) : 
            if copy_arr[i][j] == 0 :
                count += 1
    return count

for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 0 :
            empty.append([i,j])
        elif arr[i][j] == 2 :
            virus.append([i,j])

_list = list(combinations(empty, 3))

for walls in _list :
    _arr = copy.deepcopy(arr)
    for x,y in walls :
        _arr[x][y] = 1
    _arr = addVirus(_arr)
    temp_max = checkVirus(_arr)
    _max = max(_max, temp_max) 
print(_max)