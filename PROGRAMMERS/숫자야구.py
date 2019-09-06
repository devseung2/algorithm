# 프로그래머스 완전탐색 숫자야구
from itertools import permutations

def solution(baseball):
    answer = 0

    _list = list(permutations([1,2,3,4,5,6,7,8,9], 3))

    for _l in _list :
        check = True

        for b in baseball :
            b_numbers = list(map(int, str(b[0])))
            strike = 0
            ball = 0

            for _l_i in range(3) :
                for b_i in range(3) :
                    if b_numbers[b_i] == _l[_l_i] and b_i == _l_i :
                        strike += 1
                    elif b_numbers[b_i] == _l[_l_i] and b_i != _l_i:
                        ball += 1
            
            if strike != b[1] or ball != b[2] :
                check = False

        if check : 
            answer += 1

    return answer