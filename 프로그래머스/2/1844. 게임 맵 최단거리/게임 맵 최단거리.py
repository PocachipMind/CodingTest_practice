import collections

def solution(maps):
    
    #     상 하 좌 우
    dx = [ 0,0,-1, 1]
    dy = [-1,1, 0, 0]
    
    q = collections.deque([(0,0,1)])
    
    # visited = [(0,0)] 방문한곳을 이렇게 관리해도 되지만, 그냥 숫자를 갱신해도 전혀 상관없음
    # 즉 if not in 으로 방문 체크 해도 되지만 그냥 1씩 갱신해도 무관함!
    
    while q:
        v = q.popleft()
        
        if (v[0],v[1]) == (len(maps)-1,len(maps[0])-1):
            return v[2]
        
        for i in range(4):
            
            # 다음 이동 장소 설정 
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            
            # 맵 밖으로 나가는 경우
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
                
            # 방문 안한곳이라면
            if maps[nx][ny] == 1 :
                q.append((nx,ny,v[2]+1))
                maps[nx][ny] = v[2]+1
                
    # while 문 빠져나온것이라면 도착을 못하는것임.
    return -1