# 백준 15686번 문제
import itertools

N, M = map(int, input().split())
arr, house, chicken = [], [], []

for i in range(N) :
    _list = list(map(int, input().split()))
    arr.append(_list)
    for j in range(len(_list)) :
        if _list[j] == 1 :
            house.append([i,j])
        elif _list[j] == 2 :
            chicken.append([i,j])

select = itertools.combinations(chicken, M)
_min = N*N*len(house)
for sel_chicken in select :
    _sum = 0
    for h_x, h_y in house :
        house_min = N*N*len(house)
        for c_x, c_y in sel_chicken :
            house_min = min(abs(h_x-c_x)+abs(h_y-c_y), house_min)
        _sum += house_min
    _min = min(_min, _sum)

print(_min)