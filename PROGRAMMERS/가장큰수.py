# 프로그래머스 가장 큰 수
from operator import itemgetter

def solution(numbers):
    answer = ''

    numbers.sort()
    _list = numbers

    max_len = len(str(_list[len(_list)-1]))

    result = []

    for i in range(len(_list)) :
        result.append([str(_list[i]), len(str(_list[i]))])

    for val in result :
        if val[1] != max_len :
            val[0] *= (max_len - val[1] + 1)

    result.sort()

    for val in result :
        if val[1] != max_len :
            answer = val[0][0:val[1]] + answer
        else :
            answer = val[0] + answer

    return str(int(''.join(answer)))