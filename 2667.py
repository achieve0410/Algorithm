
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 5
# 01010
# 10101
# 01010
# 10101
# 01010
# 13
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1

# 4
# 0101
# 1010
# 0101
# 1010
# 8
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1


def _DFS(graph, b_graph, start, stack, visited):

    [x, y]= start
    cnt = 0

    while(x<=n-1):
        ## 집이 없으면
        if graph[x][y]!='0' and [x,y] not in visited:
            cnt+=1
            stack.append([x,y])
            while(stack):
                a,b = stack.pop()
                visited.append([a,b])
                print(a, b, stack, b_graph)
                if cnt not in b_graph:
                    b_graph[cnt]=[[a,b]]
                elif [a,b] not in b_graph[cnt]:
                    b_graph[cnt].append([a,b])

                ## 상하좌우 확인
                if a-1>=0 and graph[a-1][b]=='1' and [a-1, b] not in b_graph[cnt]:
                    stack.append([a-1, b])
                if a+1<=n-1 and graph[a+1][b]=='1' and [a+1, b] not in b_graph[cnt]:
                    stack.append([a+1, b])
                if b-1>=0 and graph[a][b-1]=='1' and [a, b-1] not in b_graph[cnt]:
                    stack.append([a, b-1])
                if b+1<=n-1 and graph[a][b+1]=='1' and [a, b+1] not in b_graph[cnt]:
                    stack.append([a, b+1])

        if y+1<=n-1:
            y+=1
        else:
            x+=1
            y=0

n = int(input())
graph = []
b_graph = {}
val = []

for _ in range(n):
    temp = str(input())
    graph.append(temp)

_DFS(graph, b_graph, [0,0], [], [])
print(len(b_graph))

for i in b_graph.values():
    val.append(len(i))
val=sorted(val)

for i in val:
    print(i)