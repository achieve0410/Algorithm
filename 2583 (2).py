# 입력
# 첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다.
# 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다.
# 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

# 출력
# 첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.

# 예제 입력 1 
# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2
# 예제 출력 1 
# 3
# 1 7 13


# 100 100 1
# 0 0 1 1

def _DFS(graph, K):

    N, M, x, y= len(graph[0]), len(graph), 0, 0
    b_graph, stack, visited = {}, [], []
    cnt = 0

    while(True):
        if graph[y][x]==0 and [y,x] not in visited:
            cnt+=1
            stack.append([y, x])
            while(stack):
                b, a = stack.pop()
                visited.append([b,a])
                if cnt not in b_graph:
                    b_graph[cnt] = [[b,a]]
                elif [b,a] not in b_graph[cnt]:
                    b_graph[cnt].append([b,a])
                
                if b-1>=0 and graph[b-1][a] == 0 and [b-1, a] not in visited:
                    stack.append([b-1, a])
                if b+1<=M-1 and graph[b+1][a] == 0 and [b+1, a] not in visited:
                    stack.append([b+1, a])
                if a-1>=0 and graph[b][a-1] == 0 and [b, a-1] not in visited:
                    stack.append([b, a-1])
                if a+1<=N-1 and graph[b][a+1] == 0 and [b, a+1] not in visited:
                    stack.append([b, a+1])
        
        if(len(b_graph)==K):
            return b_graph

        if x+1<=N-1:
            x += 1
        else:
            if y+1 <=M-1:
                y += 1
                x = 0
            else:
                return b_graph
           
M, N, K = map(int, input().split(" "))
graph = [[0 for _ in range(N)] for _ in range(M)]

if K!=1:
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split(" "))
        for idx in range(x1, x2):
            for jdx in range(y1, y2):
                graph[jdx][idx] = 1

    # for i in graph:
    #     print(i)

    b_graph=_DFS(graph, K)
    answer = []
    for i in b_graph.values():
        answer.append(len(i))

    answer = sorted(answer)

    print(len(b_graph))
    for i in answer:
        print(i, end=" ")
else:
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split(" "))
    print(1)
    print(N*M-(x2-x1)*(y2-y1))