import collections

n, m, v = map(int,input().split())

edge = collections.defaultdict(list)

visit = collections.defaultdict(bool)

for _ in range(m):
    a, b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)
    
dfs = ""

def dfsF(start,visit):
    global dfs
    if visit[start] :
        return
    visit[start] = True
    dfs += str(start) + " "
    for i in sorted(edge[start]):
        dfsF(i,visit)

dfsF(v,visit)
print(dfs)



visit = collections.defaultdict(bool)
bfs = ""

q = collections.deque()

q.append(v)
visit[v] = True
bfs += str(v) + " "

while q:
    cur = q.popleft()
    for i in sorted(edge[cur]):
        if visit[i] == False:
            q.append(i)
            visit[i] = True
            bfs += str(i) + " "
            
print(bfs)