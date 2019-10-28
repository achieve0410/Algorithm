N, M, T = list(map(int, input().split()))
plate = []
instr = []
visited = []

def roll(List, rotation, step):
    origin = [0 for _ in range(len(List))]
    if(rotation==0): ## 시계 회전
        temp = List[len(List)-step]
        for i in range(len(List)-1, 0, -1):
            if(i-step<0):
                origin[i] = List[i-step+len(List)]
            else:
                origin[i] = List[i-step]
        origin[0] = temp
    else: ## 반시계 회전
        step_2 = len(List)-step
        temp = List[len(List)-step_2]
        for i in range(len(List)-1, 0, -1):
            if(i-step_2<0):
                origin[i] = List[i-step_2+len(List)]
            else:
                origin[i] = List[i-step_2]
        origin[0] = temp

    return origin

def calcTotal(plate):
    global N, M
    total = 0

    for i in range(N):
        for j in range(M):
            if(plate[i][j]!=0):
                total += plate[i][j]
    
    if(total!=0):
        return total
    else:
        return 0

def adjust(plate):
    global N, M
    n_cnt = 0
    total = 0

    for i in range(N):
        for j in range(M):
            if(plate[i][j]!=0):
                n_cnt += 1
                total += plate[i][j]
    
    if(total==0):
        return plate
    else:
        avg = float(total/n_cnt)
        for i in range(N):
            for j in range(M):
                if(plate[i][j]!=0):
                    if(plate[i][j]>avg):
                        plate[i][j] -= 1
                    elif(plate[i][j]<avg):
                        plate[i][j] += 1
                    else:
                        continue
        return plate

def DFS(plate, x, y):
    global N, M
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    num = plate[x][y]


    q = [[x, y]]
    r = [[x, y]]
    while(q):
        t_x = q[0][0]
        t_y = q[0][1]
        if([t_x, t_y] not in r):
            r.append([t_x, t_y])
        q.pop(0)

        ## side check
        if(t_y==0):
            if(plate[t_x][0]==plate[t_x][M-1]):
                if([t_x, M-1] not in q):
                    if([t_x, M-1] not in r):
                        q.append([t_x, M-1])
        elif(t_y==M-1):
            if(plate[t_x][M-1]==plate[t_x][0]):
                if([t_x, 0] not in q):
                    if([t_x, 0] not in r):
                        q.append([t_x, 0])

        for i in range(4):
            X = t_x+dx[i]
            Y = t_y+dy[i]

            if(X<0 or X>=N or Y<0 or Y>=M):
                continue
            if(plate[X][Y]==num):    
                if([X, Y] not in q):
                    if([X, Y] not in r):
                        q.append([X, Y])
    
    return r

def check(plate):
    global N, M, T, visited
    visited = []

    for i in range(N):
        for j in range(M):
            if(plate[i][j]!=0):
                if([i, j] not in visited):
                    result = DFS(plate, i, j)
                    if(len(result)>1):
                        visited.extend(result)
            else:
                continue
    return visited

for i in range(N):
    plate.append(list(map(int, input().split())))

for i in range(T):
    instr.append(list(map(int, input().split())))

P = plate.copy()

for instruction in instr:

    # print(P, end='\n\n')
    ## 회전 xi: 판 번호 di: 방향 ki: 칸 수
    for n in range(N):
        if((n+1)%instruction[0]==0):
            P[n] = roll(P[n], instruction[1], instruction[2]) ## 시계 di=0
    
    visited = check(P)

    if(visited!=[]):
        ## 인접 숫자 삭제
        for v in visited:
            P[v[0]][v[1]]=0
    
    else:
        ## 평균 보정
        P = adjust(P)

answer = calcTotal(P)
print(answer)