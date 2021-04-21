from collections import deque

## 덩어리 체크 함수
def check(mmap):
    ## 1. for문을 돌면서 0이 아닌 값 찾기
    ## 2. 찾았을 경우 스택을 통해 덩어리 확인
    ## 3. visited & 덩어리 dictionary 유지
    ## 4. len(dictionary) return
    row, col = len(mmap), len(mmap[0])
    queue = deque()
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited_map = [[0 for _ in range(M)] for _ in range(N)]
    num, mysum, yon = 0, 0, True

    for i in range(1, row-1):
        for j in range(1, col-1):
            if mmap[i][j] != 0 and visited_map[i][j]!=1:
                queue.append([i,j])

                while(queue):
                    x, y = queue.popleft()
                    visited_map[x][y]=1
                    mysum += mmap[x][y]

                    for idx in range(4):
                        X, Y = x+dx[idx], y+dy[idx]
                        if mmap[X][Y] != 0 and visited_map[X][Y]!=1:
                            queue.append([X, Y])
                num += 1
    if mysum == 0:
        yon = False
    else:
        yon = True

    return num, yon

## 1년 지나기 함수
def nextYear(mmap):
    ## 1. for문을 돌면서 0이 아닌 값 찾기
    ## 2. 상하좌우를 보고 0의 갯수 만큼 -
    ## 3. 새로운 map으로 return

    after_map = [[0 for _ in range(M)] for _ in range(N)]
    row, col = len(mmap), len(mmap[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(1, row-1):
        for j in range(1, col-1):
            if mmap[i][j] != 0:
                temp = 0
                for idx in range(4):
                    X, Y = i+dx[idx], j+dy[idx]
                    if mmap[X][Y] == 0:
                        temp += 1
                if mmap[i][j]-temp < 0:
                    after_map[i][j] = 0
                else:                    
                    after_map[i][j] = mmap[i][j]-temp
    return after_map

## 3<= N, M <= 300
N, M = list(map(int, input().split(" ")))

## N행 M열 지도 생성
mymap = [[0 for _ in range(M)] for _ in range(N)]
for idx in range(N):
    mymap[idx] = list(map(int, input().split(" ")))


## 실제 계산
num, year, yon = 1, 0, True
while(num==1 and yon==True):
    ## 1. year += 1
    ## 2. map update
    ## 3. 덩어리 수 확인
    ## 4. 빙산이 전부 녹았는 지 확인
    year += 1
    mymap = nextYear(mymap)
    num, yon = check(mymap)

if yon==True:
    print(year)
else:
    print("0")