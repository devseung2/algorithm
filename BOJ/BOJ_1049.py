# 백준 1049번 문제
import sys

N, M = map(int, sys.stdin.readline().strip().split())

_minA = 1000
_minB = 1000

for i in range(M) :
    a, b = map(int, sys.stdin.readline().strip().split())
    _minA = min(_minA, a)
    _minB = min(_minB, b)

if N >= 6 :
    if _minA < (_minB * 6) :
        x = (N//6) * _minA
        if (N % 6) != 0 :
            if _minA < (_minB * (N%6)) :
                x += _minA
            else :
                x += (_minB * (N%6))
        print(x)
    else :
        print(N * _minB)
else :
    if _minA < (N * _minB) :
        print(_minA)
    else :
        print((N * _minB))