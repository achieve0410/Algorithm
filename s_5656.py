def countingNotZero(myMap):
    count = 0
    W = len(myMap[0])
    H = len(myMap)

    for i in range(H):
        for j in range(W):
            if(myMap[i][j]!=0):
                count += 1
    return count

def reCreateMap(myMap, block):
    if(myMap[block[0]][block[1]]==0):
        return myMap
    ret_map = myMap.copy()

    W = len(ret_map[0])
    H = len(ret_map)

    visited = []
    q = [[block[0], block[1]]]
    check = [[block[0], block[1], ret_map[block[0]][block[1]]]]

    while(q):
        row, col= q[0][0], q[0][1]
        val = ret_map[row][col]
        visited.append(q[0])
        q.pop(0)

        ## check row
        for i in range(col-(val-1), col+(val), 1):
            if(i<0 or i>=W):
                continue
            else:
                value = ret_map[row][i]
                if(value==0):
                    continue
                elif(value==1):
                    ret_map[row][i]=-1
                else:
                    if([row, i] not in q and [row, i] not in visited):
                        q.append([row, i])
                        check.append([row, i, ret_map[row][i]])

        ## check col
        for j in range(row-(val-1), row+(val), 1):
            if(j<0 or j>=H):
                continue
            else:
                value = ret_map[j][col]
                if(value==0):
                    continue
                elif(value==1):
                    ret_map[j][col]=-1
                else:
                    if([j, col] not in q and [j, col] not in visited):
                        q.append([j, col])
                        check.append([j, col, ret_map[j][col]])
    
    for i in visited:
        ret_map[i[0]][i[1]] = -1

    for i in range(W):
        if(ret_map[H-1][i]>0):
            pos = 1
        elif(ret_map[H-1][i]<0):
            pos = -1
        else:
            continue
        neg = 0
        total_neg = 0
        for j in range(H-1, -1, -1):
            if(pos==1):
                if(neg==0 and ret_map[j][i]>0):
                    continue
                else:
                    if(ret_map[j][i]<0):
                        pos = -1
                        neg = 1
                        ret_map[j][i] = 0
                    elif(ret_map[j][i]>0):
                        ret_map[j+total_neg][i] = ret_map[j][i]
                        ret_map[j][i] = 0
                        continue
                    else:
                        break
            else:
                if(ret_map[j][i]>0):
                    pos = 1
                    total_neg += neg
                    ret_map[j+total_neg][i] = ret_map[j][i]
                    ret_map[j][i] = 0
                elif(ret_map[j][i]<0):
                    neg += 1
                    ret_map[j][i] = 0
                    continue
                else:
                    break
    return ret_map

def solution(myMap, N):
    mymap = myMap.copy()
    W = len(mymap[0])
    H = len(mymap)
    N = N

    answer = W*H

    print("origin map: {}, count: {}".format(myMap, countingNotZero(myMap)))
    # q = [[4, 5], [3, 4], [4, 4]]
    q = [[0, 0], [1, 1], [2, 2], [3, 3]]

    while(N>0):
        print("\n\n")
        mymap = reCreateMap(mymap, [q[0][0], q[0][1]])
        print("{} map: {}".format(4-N, mymap))

        q.pop(0)
        temp = countingNotZero(mymap)
        print("temp: {}".format(temp))
        if(temp<answer):
            answer=temp
        N -= 1

    return answer

T = int(input())

for i in range(T):
    N, W, H = map(int, input().split())
    myMap = [0 for _ in range(H)]
    for j in range(H):
        myMap[j] = list(map(int, input().split()))
    answer = solution(myMap, N)
    print("#{} {}".format(i+1, answer))