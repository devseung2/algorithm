# 프로그래머스 완전탐색 : 모의고사
from operator import itemgetter

def solution(answers):
    _list = {1 : [1, 2, 3, 4, 5], 2 : [2, 1, 2, 3, 2, 4, 2, 5], 3 : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    _count = [[1, 0], [2, 0], [3, 0]]

    for idx, val in enumerate(answers) :
        for key in _list.keys() :
            if _list[key][int(idx%len(_list[key]))] == val : 
                _count[key-1][1] += 1

    _count.sort(key= itemgetter(1), reverse=True)

    answer = []
    max_val = _count[0][1]

    for idx in range(0, len(_count)) :
        if max_val == _count[idx][1] and _count[idx][1] != 0:
            answer.append(_count[idx][0])

    return answer