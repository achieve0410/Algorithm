## pop() : stack[LIFO], pop(0) : queue[FIFO]

def bfs(graph, start):
    # print("\n\n###### BFS ######\n\n")

    queue = [start]
    visited = []

    while queue:
        # print("visited : {}, graph = {}".format(len(visited), len(graph)))
        if( len(visited) == len(graph) ):
            break

        curr = queue.pop(0)

        if( curr not in visited ):
            visited.append(curr)
            queue += graph[curr]

    return visited

def dfs(graph, start):
    # print("\n\n###### DFS ######\n\n")

    stack = [start]
    visited = []

    while stack:
        # print("visited : {}, graph = {}".format(len(visited), len(graph)))
        if( len(visited) == len(graph) ):
            break

        curr = stack.pop()

        if( curr not in visited ):
            visited.append(curr)
            stack += graph[curr]

    return visited

def main():
    graph = { ## [Parent node, Left node, Right node]
        'A' : ['B'],
        'B' : ['A', 'C', 'H'],
        'C' : ['B', 'D'],
        'D' : ['C', 'E', 'G'],
        'E' : ['D', 'F'],
        'F' : ['E'],
        'G' : ['D'],
        'H' : ['B', 'I', 'J', 'M'],
        'I' : ['H'],
        'J' : ['H', 'K'],
        'K' : ['J', 'L'],
        'L' : ['K'],
        'M' : ['H']
    }

    start = 'A'

    b_result = bfs(graph, start)
    d_result = dfs(graph, start)

    print("bfs : {}, dfs : {}".format(b_result, d_result))


if(__name__ == '__main__'):
    main()