# 백준 대회 or 인턴

N, M, K = map(int, input().split())

max = 0

for k_n in range(K+1) :
    _n = N - k_n
    _m = M - (K - k_n)
    team = 0
    while _n >= 0 and _m >= 0 :
        _n -= 2
        _m -= 1
        if _n >= 0 and _m >= 0 :
            team += 1
            
    if max < team :
        max = team

print(max)