import collections

n, m = map(int,input().split())

mapdata = []

for _ in range(n):
    mapdata.append(list(map(int,input())))
    
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [ 0, 0, -1, 1]

q = collections.deque()

q.append((0,0))
while q:
    curx, cury = q.popleft()
    if curx == n-1 and cury == m -1:
        print(mapdata[curx][cury])
        break
    for i in range(4):
        nx = curx+dx[i]
        ny = cury+dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m and mapdata[nx][ny] == 1:
            q.append((nx,ny))
            mapdata[nx][ny] = mapdata[curx][cury]+1