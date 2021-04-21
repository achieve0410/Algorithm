## input() -> sys.stdin.readline()

from collections import deque
import sys

## 빨간 구슬/파란 구슬/구멍 위치 찾기 함수
def findLocation(mmap):
    row, col = len(mmap), len(mmap[0])

    for r in range(1, row):
        for c in range(1, col):
            if mmap[r][c]=='R':
                R = [r,c]
            if mmap[r][c]=='B':
                B = [r,c]
            if mmap[r][c]=='O':
                O = [r,c]

    return R, B, O

## 맵 출력
def printmap(mmap):
    print("\n")
    for i in mmap:
        print(i)
    print("\n")

## 판 움직이기 함수
def updateLocation(mmap, R, B, O, v):
    Rx, Ry, Bx, By, Ox, Oy = R[0], R[1], B[0], B[1], O[0], O[1]

    ## 위로 움직이기
    if v==[-1, 0]:
        ## 빨강 공 움직이기
        for i in range(Rx-1, -1, -1):
            if mmap[i][Ry]=='#':
                mmap[Rx][Ry] = '.'
                mmap[i+1][Ry] = 'R'
                break
            elif mmap[i][Ry]=='.':
                continue
            elif mmap[i][Ry]=='O':
                mmap[Rx][Ry] = '.'
                mmap[i+1][Ry] = 'RO'
                break
            elif mmap[i][Ry]=='B':
                mmap[Rx][Ry] = '.'
                mmap[i+1][Ry] = 'R'
                break

        ## 파랑 공 움직이기
        for i in range(Bx-1, -1, -1):
            if mmap[i][By]=='#':
                mmap[Bx][By] = '.'
                mmap[i+1][By] = 'B'
                break
            elif mmap[i][By]=='.':
                continue
            elif mmap[i][By]=='O':
                mmap[Bx][By] = '.'
                mmap[i+1][By] = 'BO'
                break
            elif mmap[i][By]=='R':
                mmap[Bx][By] = '.'
                mmap[i+1][By] = 'B'
                break

    # ## 아래로 움직이기
    if v==[1, 0]:
        ## 빨강 공 움직이기
        for i in range(Rx+1, len(mmap), 1):
            if mmap[i][Ry]=='#':
                mmap[Rx][Ry] = '.'
                mmap[i-1][Ry] = 'R'
                break
            elif mmap[i][Ry]=='.':
                continue
            elif mmap[i][Ry]=='O':
                mmap[Rx][Ry] = '.'
                mmap[i-1][Ry] = 'RO'
                break
            elif mmap[i][Ry]=='B':
                mmap[Rx][Ry] = '.'
                mmap[i-1][Ry] = 'R'
                break

        ## 파랑 공 움직이기
        for i in range(Bx+1, len(mmap), 1):
            if mmap[i][By]=='#':
                mmap[Bx][By] = '.'
                mmap[i-1][By] = 'B'
                break
            elif mmap[i][By]=='.':
                continue
            elif mmap[i][By]=='O':
                mmap[Bx][By] = '.'
                mmap[i-1][By] = 'BO'
                break
            elif mmap[i][By]=='R':
                mmap[Bx][By] = '.'
                mmap[i-1][By] = 'B'
                break

    ## 왼쪽으로 움직이기
    if v==[0, -1]:
        ## 빨강 공 움직이기
        for i in range(Rx-1, -1, -1):
            if mmap[Rx][i]=='#':
                mmap[Rx][Ry] = '.'
                mmap[Rx][i+1] = 'R'
                break
            elif mmap[Rx][i]=='.':
                continue
            elif mmap[Rx][i]=='O':
                mmap[Rx][Ry] = '.'
                mmap[Rx][i+1] = 'RO'
                break
            elif mmap[Rx][i]=='B':
                mmap[Rx][Ry] = '.'
                mmap[Rx][i+1] = 'R'
                break

        ## 파랑 공 움직이기
        for i in range(Bx-1, -1, -1):
            if mmap[Bx][i]=='#':
                mmap[Bx][By] = '.'
                mmap[Bx][i+1] = 'B'
                break
            elif mmap[Bx][i]=='.':
                continue
            elif mmap[Bx][i]=='O':
                mmap[Bx][By] = '.'
                mmap[Bx][i+1] = 'BO'
                break
            elif mmap[Bx][i]=='R':
                mmap[Bx][By] = '.'
                mmap[Bx][i+1] = 'B'
                break

    ## 오른쪽으로 움직이기
    if v==[0, 1]:
        ## 빨강 공 움직이기
        for i in range(Rx+1, len(mmap[0]), 1):
            if mmap[Rx][i]=='#':
                mmap[Rx][Ry] = '.'
                mmap[Rx][i-1] = 'R'
                break
            elif mmap[Rx][i]=='.':
                continue
            elif mmap[Rx][i]=='O':
                mmap[Rx][Ry] = '.'
                mmap[Rx][i-1] = 'RO'
                break
            elif mmap[Rx][i]=='B':
                mmap[Rx][Ry] = '.'
                mmap[Rx][i-1] = 'R'
                break

        ## 파랑 공 움직이기
        for i in range(Bx-1, -1, -1):
            if mmap[Bx][i]=='#':
                mmap[Bx][By] = '.'
                mmap[Bx][i-1] = 'B'
                break
            elif mmap[Bx][i]=='.':
                continue
            elif mmap[Bx][i]=='O':
                mmap[Bx][By] = '.'
                mmap[Bx][i-1] = 'BO'
                break
            elif mmap[Bx][i]=='R':
                mmap[Bx][By] = '.'
                mmap[Bx][i-1] = 'B'
                break

    return mmap


## 3<=N,M<=10
N, M = list(map(int, input().split(" ")))

myarray = [0 for _ in range(N)]
for i in range(N):
    myarray[i] = list(map(str, input()))

printmap(myarray)

## 1. 빨간 구슬/파란 구슬/구멍 위치 찾기
# mR, mB, mO = findLocation(myarray)
# print(mR, mB, mO)

## 2. 판 움직이기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for idx in range(4):
    v = [dx[idx], dy[idx]]
    mR, mB, mO = findLocation(myarray)
    print(mR, mB, mO)
    myarray = updateLocation(myarray, mR, mB, mO, v)
    printmap(myarray)

## 3. 
