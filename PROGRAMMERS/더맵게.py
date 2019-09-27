# 프로그래머스 더 맵게
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K and len(scoville) > 1 :
        s1, s2 = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, s1+(s2*2))
        answer += 1
    if scoville[0] < K :
        return -1
    return answer