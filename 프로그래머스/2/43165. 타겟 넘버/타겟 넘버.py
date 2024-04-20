answer = 0
def solution(numbers, target):
    numlen = len(numbers)-1
    
    def dfs(num, now):
        global answer
        if now == numlen:
            if num == target:
                answer += 1
            return
        dfs(num+numbers[now+1],now+1)
        dfs(num-numbers[now+1],now+1)
        
    dfs(numbers[0],0)
    
    dfs(-numbers[0],0)
    
    return answer