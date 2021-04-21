
# 입력
# 첫째 줄에는 테스트케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 주어진다.
# 첫째 줄에 건물의 개수 N 과 건물간의 건설순서규칙의 총 개수 K이 주어진다.
# (건물의 번호는 1번부터 N번까지 존재한다) 

# 둘째 줄에는 각 건물당 건설에 걸리는 시간 D가 공백을 사이로 주어진다.
# 셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. 
# (이는 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미이다) 

# 마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다.

# 출력
# 건물 W를 건설완료 하는데 드는 최소 시간을 출력한다.
# 편의상 건물을 짓는 명령을 내리는 데는 시간이 소요되지 않는다고 가정한다.

# 건설순서는 모든 건물이 건설 가능하도록 주어진다.

# 제한
# 2 ≤ N ≤ 1000
# 1 ≤ K ≤ 100,000
# 1 ≤ X, Y, W ≤ N
# 0 ≤ D ≤ 100,000, D는 정수

# 예제 입력 1 
# 2
# 4 4
# 10 1 100 10
# 1 2
# 1 3
# 2 4
# 3 4
# 4
# 8 8
# 10 20 1 5 8 7 1 43
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 5 7
# 6 7
# 7 8
# 7
# 예제 출력 1 
# 120
# 39

from collections import deque

def checking(visited, myarray):

    for point in myarray:
        if visited[point-1]!=1:
            return 0
    
    return 1


## T: 테케 갯수
T = int(input())

for _ in range(T):
    ## N: 건물 갯수(1-N), K:건설 순서 규칙의 갯수 
    N, K = list(map(int, input().split(" ")))

    ## 건설 시간 배열
    mytime = list(map(int, input().split(" ")))

    ## 규칙 메모 배열
    # myrule = [0 for _ in range(N)]
    _rule = [[0 for _ in range(N)] for _ in range(N)]

    ## 시작/끝 찾기 배열
    start = {}
    end = {}
    _start = [0 for _ in range(N)]    

    ## 규칙 추가
    for idx in range(K):
        x, y = list(map(int, input().split(" ")))
        # myrule[idx] = [x,y]
        _rule[x-1][y-1] = 1

        if x not in start:
            start[x] = [y]
        else:
            start[x].append(y)
        
        if y not in end:
            end[y] = [x]
        else:
            end[y].append(x)
        
        _start[y-1] = 1
        
    ## 지어야 할 건물
    W = int(input())

    print(start)
    print(end)
    # print(_start)

    ## 건설 시작 건물
    srt = -1
    for idx in range(N):
        if _start[idx] == 0:
            srt = idx+1
    
    print(srt)
    ## 첫 건물 시간으로부터 시작
    answer = mytime[srt-1]

    ## 건설 시작
    queue = deque()
    queue.append(srt)
    _end = 0
    visited = [0 for _ in range(N)]
    
    while queue:
        ## 방문처리 및 종료 조건 설정
        p = queue.popleft()
        print("p: ", p)
        if p == W:
            break
        # elif visited[p-1] == 1:
        #     continue
        visited[p-1] = 1

        ## 다음 건설 건물 시간 더하기
        tmp = -1

        ## p로부터 갈 수 있는 점들이 있다면
        if p in start:
            ## p로부터 갈 수 있는 점들에 대해서
            for nxt in start[p]:
                ## 방문하지 않은 점들에 대해서
                if visited[nxt-1] != 1:
                    ## 당장 건설을 할 수 있다면
                    if checking(visited, end[nxt])==1:
                        print("!!")
                        # print(visited)
                        # print(end[nxt])
                        queue.append(nxt)
                        visited[nxt-1] = 1
                        if tmp<=mytime[nxt-1]:
                            tmp = mytime[nxt-1]
                    else:
                        print("@@")
                        # print(visited)
                        # print(end[nxt])
                        continue
        else:
            print("no")
            continue
        
        if tmp!=-1:
            print(tmp)
            answer += tmp
    # print(mytime)
    # print(myrule)
    # print(_rule)

    print(answer)
