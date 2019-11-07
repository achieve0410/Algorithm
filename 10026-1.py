import sys

def BFS(points):    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = set()

    q.add(points)

    while(q):
        point = q.pop()

        xx, yy = point[0], point[1]
        color = Map[xx][yy]

        visited.add(point)

        for i in range(4):
            x = xx + dx[i]
            y = yy + dy[i]

            if( x<0 or x>N-1 or y<0 or y>N-1 ):
                continue
            else:
                if(Map[x][y] == color):
                    if(tuple([x,y]) not in visited):
                        if(tuple([x,y]) not in q):
                            q.add(tuple([x,y]))

def BFS2(points):    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = set()

    q.add(points)

    while(q):
        point = q.pop()

        xx, yy = point[0], point[1]
        color = Map[xx][yy]

        visited2.add(point)

        for i in range(4):
            x = xx + dx[i]
            y = yy + dy[i]

            if( x<0 or x>N-1 or y<0 or y>N-1 ):
                continue
            else:
                ## Blue
                if(color == 'B'):
                    if(Map[x][y] == color):
                        if(tuple([x,y]) not in visited2):
                            if(tuple([x,y]) not in q):
                                q.add(tuple([x,y]))

                ## Red Green
                else:
                    if(Map[x][y] != 'B'):
                        if(tuple([x,y]) not in visited2):
                            if(tuple([x,y]) not in q):
                                q.add(tuple([x,y]))

def solution():
    answer1, answer2 = 0, 0

    for i in range(N):
        for j in range(N):
            if(tuple([i, j]) not in visited):
                answer1 += 1
                BFS(tuple([i, j]))
            if(tuple([i, j]) not in visited2):
                answer2 += 1
                BFS2(tuple([i, j]))
            

    return answer1, answer2

if(__name__=='__main__'):
    global visited, visited2, temp, N, Map

    N = int(sys.stdin.readline())
    Map = []
    for i in range(N):
        Map.extend(sys.stdin.readline().split())
    # print(Map)
    visited = set()
    visited2 = set()
    temp = set()

    ans1, ans2 = solution()
    print(ans1, ans2)