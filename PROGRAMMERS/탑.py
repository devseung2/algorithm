# 프로그래머스 스택 탑

def solution(heights):
    answer = []

    for i in range(len(heights), 0, -1) :
        pop = heights.pop(len(heights)-1)
        
        for j in range(len(heights)-1, -1, -1) :
            if pop < heights[j] :
                answer.insert(0, j+1)
                break
            elif j == 0 :
                answer.insert(0, 0)

    answer.insert(0, 0)
    
    return answer

solution([6,9,5,7,4])