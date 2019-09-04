# Level1 완주하지 못한 선수

def solution(participant, completion): 
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)) :
        if i == len(participant)-1 or participant[i] != completion[i] :
            return participant[i]