import collections

def solution(begin, target, words):
        
    # target이 리스트 안에 있는지 부터 확인
    if target not in words:
        return 0
    
    def can_transe(start,end):
        # 서로 길이 다르면 False
        if len(start) != len(end):
            return False
        
        # 2개이상 다르면 False
        count = 0
        for indx,ch in enumerate(start):
            if end[indx] != ch :
                count += 1
        if count != 1 :
            return False
        else :
            # 아니면 True
            return True

        
    # 여기부터 BFS 구현
    
    q = collections.deque()
    
    q.append((begin,0))
    
    while q :
        now, dist = q.popleft()
        
        if now == target:
            return dist
        
        for i in words:
            if can_transe(now,i):
                q.append((i,dist+1))