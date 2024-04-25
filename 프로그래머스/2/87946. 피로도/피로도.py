from collections import deque

def bfs(start, k, dungeons):
    queue = deque()
    queue.append([start, k, 0, [False for _ in range(len(dungeons))]])
    counted = []
    
    while queue:
        location, tired, count, visited = queue.popleft()
        visited[location] = True
        tired -= dungeons[location][1]
        count += 1
        counted.append(count)
        
        for i in range(len(dungeons)):
            if not visited[i] and tired >= dungeons[i][0]:
                queue.append([i, tired, count, visited[:]])
                
    return max(counted)

def solution(k, dungeons):
    answer = -1
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            answer = max(answer, bfs(i, k, dungeons))
    return answer