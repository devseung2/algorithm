# 백준 라면공장
import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    h = []
    idx = 0
    while stock < k :
        for i in range(idx, len(dates)) :
            if dates[i] <= stock :
                heapq.heappush(h, -supplies[i])
                idx += 1
            else :  
                break 
        stock += -heapq.heappop(h)
        answer += 1
    return answer