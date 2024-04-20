def solution(nums):
    pick = len(nums)//2
    nums = set(nums)
    if pick >= len(nums):
        return len(nums)
    else :
        return pick
    
    return answer
