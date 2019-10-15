# 백준 1010번 문제
import itertools

T = int(input())

for i in range(T) :
    N, M = map(int, input().split())
    l = M-N
    _N, _M = 1, 1
    for j in range(l) :
        _M *= M
        _N *= M-N
        M -= 1

    print(_M//_N)