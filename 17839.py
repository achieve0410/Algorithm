import sys
sys.setrecursionlimit(100000)

a_set = set()

def DFS(word, Dict):
    global a_set

    if(word not in Dict):
        return

    for i in Dict[word]:
        a_set.add(i)
        DFS(i, Dict)

def solution(cmd):
    global a_set

    myDict = {}
    flag = 0

    for i in range(len(cmd)):
        c_key = cmd[i][0]
        c_value = cmd[i][2]
        
        if(c_key=='Baba'):
            flag=1

        if(c_key not in myDict):
            myDict[c_key] = [c_value]
        else:
            myDict[c_key].append(c_value)

    if(flag==1):
        for i in myDict['Baba']:
            a_set.add(i)
            DFS(i, myDict)
    else:
        return []

    return sorted(a_set)

if(__name__=='__main__'):
    N = int(input())
    answer = []
    cmd = []
    for i in range(N):
        cmd.append(input().split(' '))
    # print(cmd)

    answer = solution(cmd)
    for i in answer:
        print(i, end='\n')
        
