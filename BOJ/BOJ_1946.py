# 백준 알고리즘 1946 번 문제
import sys

T = int(sys.stdin.readline().strip())

for i in range(T) :
    N = int(sys.stdin.readline().strip())
    arr = [0 for i in range(N+1)]

    for j in range(N) :
        idx, val = map(int, sys.stdin.readline().strip().split())
        arr[idx] = val
 
    check = 1
    _min = arr[1]

    for j in range(2, N+1) :
        if arr[j] < _min :
            _min = arr[j]
            check += 1

        if _min == 1 :
            break
    print(check)