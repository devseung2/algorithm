# 프로그래머스 완전탐색 소수 찾기
import itertools

def solution(numbers):
    answer = 0
    _list = []

    for i in range(1, len(numbers)+1) :
        _list += list(map(int, set(map(''.join, itertools.permutations(list(numbers), i)))))

    for val in list(set(_list)): 
        check = True

        for i in range(2, val) :
            if (val % i) == 0 :
                check = False
                break

        if check and val > 1 :
            answer += 1

    return answer