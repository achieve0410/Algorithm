import sys

def parallendrom(myarray, first, second, memtable):
    length = second-first+1

    if memtable[first-1][second-1]==1:
        return 1
    elif length==1:
        memtable[first-1][second-1]=1
        return 1
    elif length==2:
        if myarray[first-1]!=myarray[second-1]:
            return 0
    else:
        for idx in range(length//2):
            if memtable[first+idx-1][second-idx-1]==1:
                memtable[first-1][second-1]=1
                return 1
            elif myarray[first+idx-1] != myarray[second-idx-1]:
                return 0
    
    memtable[first-1][second-1]=1
    return 1


N = int(sys.stdin.readline())
myarray = list(map(int, sys.stdin.readline().split(" ")))
memtable = [[0 for i in range(N)] for j in range(N)]

M = int(sys.stdin.readline())

for _ in range(M):
    first, second = list(map(int, sys.stdin.readline().split(" ")))
    print(parallendrom(myarray, first, second, memtable))