# 백준 1018번 문제
import sys

M, N = map(int, (sys.stdin.readline().strip().split()))
arr = [list(str(input())) for i in range(M)]
_min = 64

for m_start in range(M-7) :
    for n_start in range(N-7) :
        for k in range(2) :
            _sum = 0
            for i in range(m_start, m_start+8) :
                for j in range(n_start, n_start+8) :
                    if (k == 0 and i % 2 == 0) or (k == 1 and i % 2 == 1) :
                        if j % 2 == 0 and arr[i][j] == 'B' or j % 2 == 1 and arr[i][j] == 'W':
                            _sum += 1
                    else :
                        if j % 2 == 0 and arr[i][j] == 'W' or j % 2 == 1 and arr[i][j] == 'B':
                            _sum += 1

            _min = min(_sum, _min)

print(_min)