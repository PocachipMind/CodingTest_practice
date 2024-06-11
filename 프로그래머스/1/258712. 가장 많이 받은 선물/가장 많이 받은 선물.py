def solution(friends, gifts):
    alls = dict()
    for i in friends:
        alls[i] = [0,0,0]
        
    check = dict()
    for i in friends:
        check[i] = dict()
        for j in friends:
            check[i][j] = 0
    
    
    for i in gifts:
        a, b = i.split()
        alls[a][0] += 1
        alls[b][1] += 1
        check[a][b] += 1
        
    
    for i in alls:
        alls[i][2] = alls[i][0]-alls[i][1]
    
    data = -1
    for i in friends:
        cur = 0
        for j in friends:
            if check[i][j] > check[j][i]:
                cur += 1
            elif check[i][j] == check[j][i]:
                if alls[i][2] > alls[j][2]:
                    cur += 1
        
        if cur>data:
            data = cur
            
    
    
    return data