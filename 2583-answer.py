import sys

input = sys.stdin.readline

di = [0,1,0,-1]
dj = [1,0,-1,0]


def bfs(i,j,n,m):
    q = []
    q.append((i,j))
    visited[i][j] = 1
    cnt = 1
    while(q):
        x, y = q.pop(0)
        for i in range(4):
            dx = x + di[i]
            dy = y + dj[i]
            if(0<=dx and dx<m and 0<=dy and dy<n):
                if(pap[dx][dy] == 1 and visited[dx][dy] == 0 ):
                    visited[dx][dy] = 1
                    q.append((dx,dy))
                    cnt += 1
    return cnt
m, n, k = map(int, input().split())

pap = [[1]*n for i in range(m)]

for p in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            pap[i][j] = 0

# print(*pap, sep="\n")

visited = [[0]*n for i in range(m)]
res = []
for i in range(m):
    for j in range(n):
        if(pap[i][j] == 1 and visited[i][j] == 0):
            res.append(bfs(i,j,n,m))

# print(*visited, sep="\n")
print(len(res))
print(*sorted(res), sep=" ")