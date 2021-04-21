
from collections import deque
import sys

def checkMap(mmap):
    rows, cols = len(mmap), len(mmap[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[0 for _ in range(cols)]for _ in range(rows)]
    queue = deque()
    sheeps, wolfs = 0, 0

    for row in range(rows):
        for col in range(cols):
            if visited[row][col] == 0:
                if mmap[row][col] == 'o' or mmap[row][col] == 'v':
                    sheep, wolf = 0, 0

                    queue.append([row, col])
                    while queue:
                        x, y = queue.popleft()
                        visited[x][y] = 1

                        if mmap[x][y] == 'o':
                            sheep += 1
                        elif mmap[x][y] == 'v':
                            wolf += 1

                        for i in range(4):
                            X, Y = x+dx[i], y+dy[i]

                            if X>=0 and X<rows and Y>=0 and Y<cols:
                                if mmap[X][Y] != '#':
                                    if visited[X][Y]==0 and [X, Y] not in queue:
                                        queue.append([X, Y])
                    if sheep>wolf:
                        sheeps += sheep
                    else:
                        wolfs += wolf

                else:
                    continue
    return [sheeps, wolfs]

## 3 <= R,C <= 250
R, C = list(map(int, sys.stdin.readline().split(" ")))

## 지도 배열
mymap = [[0 for _ in range (C)]for _ in range(R)]
row, col = len(mymap), len(mymap[0])

for idx in range(row):
    mymap[idx] = list(map(str, sys.stdin.readline()))

## 지도를 돌며 양의 수와 늑대의 수 확인
print(checkMap(mymap)[0], checkMap(mymap)[1])