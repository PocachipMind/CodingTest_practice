from collections import deque
def solution(maps):
    
    maxx = len(maps)-1
    maxy = len(maps[0])-1
    
    q = deque()
    
    #     상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]
    
    q.append((0,0,1))
    
    while q:
        curx, cury, d = q.popleft()
        
        if curx == maxx and cury == maxy:
            return d
        
        for i in range(4):
            if 0 <= curx + dx[i] <= maxx and 0 <= cury + dy[i] <= maxy and maps[curx + dx[i]][cury + dy[i]] == 1:
                q.append((curx + dx[i],cury + dy[i],d+1))
                maps[curx + dx[i]][cury + dy[i]] = d+1
    
    

    return -1