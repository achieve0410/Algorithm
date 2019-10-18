import sys
import copy

myMap = []
virusList = []
N, M = 0, 0
maxVal = 0

def getSafeArea(Map):
    return

def spreadVirus(X, Y, Map):
    return

def buildWall(start, count):
    global maxVal

    if(count==3):
        # Map = copy.deepcopy(myMap)

        # while(virusList):
        #     [vX, vY] = virusList[0]
        #     virusList.pop(0)
        #     spreadVirus(vX, vY, Map)
        
        # maxVal = max(maxVal, getSafeArea(Map))
        return
    
    for i in range(start, N*M):
        x = int(i/M)
        y = int(i%M)
        print("x, y: {}, {}".format(x, y))

        if(myMap[x][y] == 0):
            myMap[x][y] = 1
            buildWall(i+1, count+1)
            myMap[x][y] = 0

if( __name__ == '__main__'):
    N, M = map(int, sys.stdin.readline().split())
    for i in range(N):
        myMap.append(list(map(int, sys.stdin.readline().split())))
    
    for i in range(N):
        for j in range(M):
            if(myMap[i][j] == 2):
                virusList.append([i, j])
    
    buildWall(0, 0)
    print(maxVal)


print(myMap)