import itertools

def solution(numbers, target):
    answer = 0
    pick = [-1, 1]
    alls = list(itertools.product(pick,repeat=len(numbers)))
    
    for i in alls:
        cur = 0
        for j in enumerate(i):
            if j[1] > 0:
                cur += numbers[j[0]]
            else:
                cur -= numbers[j[0]]
        if cur == target:
            answer += 1
    
    
    return answer