## 마트 평촌
## sk 01041800637
## 

def DFS(graph, start): ## stack
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort(reverse=True)
                stack += tmp
    
    return " ".join(str(n) for n in visited)


def BFS(graph, start): ## queue
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)

        if n not in visited:
            visited.append(n)

            if n in graph:
                tmp = list(set(graph[n])-set(visited))
                tmp.sort()
                queue+=tmp

    return " ".join(str(i) for i in visited)






graph = {} ## dictionary for graph data
iput = input().split(' ')
N, M, V = [int(i) for i in iput]

for i in range(M):
    m = input().split(' ')
    m1, m2 = [int(j) for j in m]

    if m1 not in graph:
        graph[m1] = [m2]
    elif m2 not in graph[m1]:
        graph[m1].append(m2)

    if m2 not in graph:
        graph[m2] = [m1]
    elif m1 not in graph[m2]:
        graph[m2].append(m1)

    # print(graph)

print(DFS(graph, V))
print(BFS(graph, V))


# def main():

#     N, M, V = map(int, input('input: ').split())

#     array = [[0,0] for _ in range(M)]
#     for i in range(M):
#         array[i]=list(map(int, input().split()))

#     ## print(array)


#     ## Result of DFS
#     visited = []
#     DFS(visited, array, V)


#     ## init
#     ##init()

#     ## Result of BFS
#     ##BFS(N, M, V)


# if (__name__ == "__main__"):
# 	main()