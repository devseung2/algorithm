# 프로그래머스 K번째 수

def solution(array, commands):

    answer = []

    for i, j, k in commands :
        _list = array[i-1:j]
        _list.sort()
        answer.append(_list[k-1])

    return answer