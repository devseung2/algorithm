# 프로그래머스 스택 쇠막대기

def solution(arrangement):
    list_a = list(arrangement)
    stack = []
    answer = 0
    last = ''
    for s in list_a :
        if s == '(' : 
            stack.append(s)
            last = s
        else :
            stack.pop()
            if last == '(' :
                answer += len(stack)
                last = s
            else : 
                answer += 1
    
    return answer

solution("()(((()())(())()))(())")
# solution("()(()(()))")