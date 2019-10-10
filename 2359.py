import sys

count = 0

minValue = 0
maxValue = 0
totalCost = 0
ways = []

t_minValue = 0
t_maxValue = 0
t_totalCost = 0
t_ways = [] 

def bst(road, start, cost):

    global t_minValue
    global t_maxValue
    global t_totalCost

    global count

    if(count==0):
        for idx, cost in enumerate(road[start-1]):
            if(cost==0):
                continue
            else:
                bst(road, idx, cost)
    else:
        if(cost<t_minValue):
            t_totalCost += (t_minValue-cost)
        elif(cost>t_maxValue):
            t_totalCost += (cost-t_maxValue)
        else:
            t_totalCost += 0

        for idx, cost in enumerate(road[start-1]):
            if(cost==0):
                continue
            else:
                bst(road, idx, cost)



def solution(road, S, T):
    costs = []
    ways = []

    global count

    for idx, cost in enumerate(road[S-1]):
        count = 0        
        if(cost==0):
            continue
        else:
            bst(road, idx, cost)
            
        


        



    return answer

n, m, S, T = map(int, sys.stdin.readline().split())

road = [[0]*n for i in range(n)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    road[a-1][b-1]=c


answer = solution(road, S, T)
print(answer)