
from collections import deque


def BFS(graph):

    queue = deque()
    queue.append(1)
    visited = []

    while(queue):
        p=queue.popleft()
        visited.append(p)

        for value in graph[p]:
            if value not in visited and value not in queue:
                queue.append(value)
    
    # print(visited)

    return len(visited)-1


N = int(input())
K = int(input())
myarray, b_graph = [], {}

for _ in range(K):
    cc = list(map(int, input().split(" ")))
    if cc[0] not in b_graph:
        b_graph[cc[0]]=[cc[1]]
        if cc[1] not in b_graph:
            b_graph[cc[1]]=[cc[0]]
        else:
            b_graph[cc[1]].append(cc[0])
    else:
        b_graph[cc[0]].append(cc[1])
        if cc[1] not in b_graph:
            b_graph[cc[1]]=[cc[0]]
        else:
            b_graph[cc[1]].append(cc[0])
    myarray.append(cc)

# print(myarray)
# print(b_graph)

answer = BFS(b_graph)
print(answer)