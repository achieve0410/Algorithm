import sys
N, M, count, answer = 0, 0, 0, 0
Map = []
two = set()
visited = set()
v_visited = set()

def return_map():
    for i in range(N):
        for j in range(M):
            if(Map[i][j]==2):
                if(tuple([i,j]) not in two):
                    Map[i][j]=0

def spread_virus():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for t in two:
        q = set()
        q.add(t)

        while(q):
            point = q.pop()
            xx = point[0]
            yy = point[1]

            for i in range(4):
                x = xx + dx[i]
                y = yy + dy[i]

                if( x<0 or x>=N or y<0 or y>=M ):
                    continue
                else:
                    if(Map[x][y]==0):
                        Map[x][y]=2
                        q.add(tuple([x,y]))

def two_count():
    global two

    for i in range(N):
        for j in range(M):
            if(Map[i][j]==2):
                two.add(tuple([i, j]))


def zero_count():
    # for i in Map:
    #     print(i, end='\n')
    cnt = 0

    for i in range(N):
        for j in range(M):
            if(Map[i][j]==0):
                cnt += 1

    return cnt

def BFS():
    global count, answer

    for i in range(N):
        for j in range(M):
            if(tuple([i, j]) not in visited):
                if(Map[i][j]==0):
                    if(count==1):
                        Map[i][j]=1
                        count += 1
                        BFS()
                        Map[i][j]=0
                        count -= 1

                    elif(count==2):
                        Map[i][j]=1

                        spread_virus()

                        temp = zero_count()
                        if(temp>answer):
                            answer = temp

                        return_map()
                        Map[i][j]=0
                        
def solution():
    global count

    two_count()

    for i in range(N):
        for j in range(M):
            if(Map[i][j]==0):
                visited.add(tuple([i, j]))
                Map[i][j]=1
                count += 1

                BFS()

                Map[i][j]=0
                count -= 1

if( __name__ == '__main__'):
    N, M = list(map(int, sys.stdin.readline().split()))

    for i in range(N):
        Map.append(list(map(int, sys.stdin.readline().split())))

    # print(Map, end='\n')
    
    solution()
    print(answer)