
from collections import deque
import sys

# def printMap(mmap):
#     for i in mmap:
#         print(i)


def calcSafe(mmap, first, second, third):
    N, M = len(mmap), len(mmap[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue = deque()
    visited = set()

    one, two = 0, 0

    for row in range(N):
        for col in range(M):

            if mmap[row][col] == 2 and tuple([row, col]) not in visited:
                queue.append([row, col])

                while queue:
                    x, y = queue.popleft()
                    two += 1
                    visited.add(tuple([x,y]))

                    for i in range(4):
                        X, Y = x+dx[i], y+dy[i]

                        if X>=0 and X<N and Y>=0 and Y<M:
                            if mmap[X][Y] == 0 and [X, Y] not in queue and tuple([X, Y]) not in visited:
                                queue.append([X,Y])
            elif mmap[row][col] == 1:
                one += 1            
            else:
                continue

    return N*M-one-two

## 3 ≤ N, M ≤ 8
N, M = list(map(int, sys.stdin.readline().split(" ")))

myset = set()
mymap = [[0 for _ in range(M)] for _ in range(N)]

rows, cols = len(mymap), len(mymap[0])
for row in range(rows):
    mymap[row] = list(map(int, sys.stdin.readline().split()))

length = N*M
answer, temp = 0, 0
for first in range(0, length):
    x1, y1 = first//M, first%M
    if mymap[x1][y1] == 0:
        mymap[x1][y1] = 1
        for second in range(first+1, length):
            x2, y2 = second//M, second%M
            if mymap[x2][y2] == 0:
                mymap[x2][y2] = 1
                for third in range(second+1, length):
                    x3, y3 = third//M, third%M
                    if mymap[x3][y3] == 0:
                        mymap[x3][y3] = 1
                        myset.add(tuple([first, second, third]))
                        temp = calcSafe(mymap, first, second, third)
                        if answer <= temp:
                            answer = temp
                        mymap[x3][y3] = 0
                mymap[x2][y2] = 0
        mymap[x1][y1] = 0
    ## mymap[x1][y1]!=0:
    else:
        continue

print(answer)
