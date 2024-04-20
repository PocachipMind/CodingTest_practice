from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    def bfs(graph, start, visited):
        q = deque([start]) 
        # 처음 부분 방문 처리
        visited[start] = True
        # 큐가 빌때까지 반복
        while q:
            v = q.popleft()
            # print(v, end=" ")
            for i in range(n):
                if i == v:
                    continue
                if computers[v][i] == 1:
                    if not visited[i]:
                        q.append(i)
                        visited[i] = True
            
    for i in range(n):
        if visited[i] == False:
            bfs(computers, i, visited)
            answer += 1
    
    
    return answer