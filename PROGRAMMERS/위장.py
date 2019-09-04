# 프로그래머스 Level2 위장

from collections import Counter

def solution(clothes):
    clothes_list = Counter([value for key, value in clothes])

    count = 1

    for val in clothes_list.values() :
        count *= (val + 1)

    return count-1