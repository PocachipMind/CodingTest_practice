def solution(n, computers):
    answer = 0
    visit = [False] * n
    
    def dfs(start,visit,computers):
        if not visit[start] : # 방문 안했다면 방문했다고 체크
            visit[start] = True
            for nextnode, cango in enumerate(computers[start]):
                if nextnode != start and cango == 1:
                    dfs(nextnode,visit,computers)
    
    for i in range(n):
        if not visit[i] :
            dfs(i,visit,computers)
            answer+= 1
    
    return answer