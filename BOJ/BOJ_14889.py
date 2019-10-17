# 백준 14889번 문제
import itertools

N = int(input())
arr = []
team = [0 + _ for _ in range(N)]
_min = 1000

for i in range(N) :
    arr.append(list(map(int, input().split())))

_team = list(itertools.combinations(team, N//2))
for i in range((len(_team))//2) :
    start = list(itertools.combinations(_team[i], 2))
    link = list(itertools.combinations(_team[len(_team)-i-1], 2))
    sum_start, sum_link = 0, 0
    
    for j in range(len(start)) :
        start_i, start_j = start[j]
        link_i, link_j = link[j]

        sum_start += arr[start_i][start_j] + arr[start_j][start_i]
        sum_link += arr[link_i][link_j] + arr[link_j][link_i]
    _min = min(abs(sum_start-sum_link), _min)

print(_min)