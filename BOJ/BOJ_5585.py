# 백준 알고리즘 5585번 문제

def changesCount(m_list, changes) :
    idx = 0
    count = 0
 
    while changes != 0 :
        if int(changes / m_list[idx]) != 0 :
            count += int(changes / m_list[idx])
            changes = changes % m_list[idx]

        idx += 1

    return count

money = 1000

m_list = [500, 100, 50, 10, 5, 1]

itemPrice = int(input())

changes = money - itemPrice

print(changesCount(m_list, changes))