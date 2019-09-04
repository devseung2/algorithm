# 프로그래머스 Level2 프린터

def solution(priorities, location):
    
    index_list = []

    for i in range(len(priorities)) :
        index_list.append(i)

    _list = []

    for x, y in zip(priorities, index_list) :
        _list.append([x, y])

    result = []

    count = 0

    while _list : 
        check = False
        pop_priority, pop_location = _list.pop(0)

        print(pop_priority, pop_location, location)

        if _list :
            max_priority, max_location = max(_list)

            if pop_priority >= max_priority :
                count += 1
                check = True
            else : 
                _list.append([pop_priority, pop_location])
        else :
            count += 1

        if pop_location == location and check:
            break
            
    return count