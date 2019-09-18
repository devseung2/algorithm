# 백준 1049번 문제
import sys

N, M = map(int, sys.stdin.readline().strip().split())

_minA = 1000
_minB = 1000

for i in range(M) :
    a, b = map(int, sys.stdin.readline().strip().split())
    _minA = min(_minA, a)
    _minB = min(_minB, b)

# N이 6 이상일 때
if N >= 6 :
    # 패키지가격 < 낱개로 6개 산 가격 (즉, 6개씩 살때 패키지 가격으로 구매)
    if _minA < (_minB * 6) :
        x = (N//6) * _minA
        # N개를 6으로 나누고 나머지가 있는 경우 
        if (N % 6) != 0 :
            # 패키지가격 < 나머지를 낱개로 산 가격 (즉, 나머지를 패키지 가격으로 구매)
            if _minA < (_minB * (N%6)) :
                x += _minA
            # 패키지가격 >= 나머지를 낱개로 산 가격 (즉, 나머지를 낱개 가격으로 구매)
            else :
                x += (_minB * (N%6))
        print(x)
    # 패키지가격 >= 낱개로 6개 산 가격
    else :
        print(N * _minB)
# N이 6 미만일 때
else :
    # 패키지 가격 < N개 * 낱개 가격 (즉, 패키지가격으로 구매)
    if _minA < (N * _minB) :
        print(_minA)
    # 패키지 가격 >= N개 * 낱개 가격 (즉, 낱개 가격으로 N개 구매)
    else :
        print(N * _minB)