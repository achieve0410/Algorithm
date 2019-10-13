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
    ret_map = myMap.copy()

    W = len(ret_map[0])
    H = len(ret_map)

    visited = []
    r = []
    q = [[block[0], block[1]]]

    while(q):
        row, col= q[0][0], q[0][1]
        val = ret_map[row][col]
        visited.append(q[0])
        q.pop(0)
        if(row not in r):
            r.append(row)

        ## check row
        for i in range(col-(val-1), col+(val), 1):
            if(i<0 or i>=W):
                continue
            else:
                value = ret_map[row][i]
                if(value==0):
                    continue
                elif(value==1):
                    ret_map[row][i]=0
                else:
                    if([row, i] not in q and [row, i] not in visited):
                        q.append([row, i])
        
        ## check col
        for j in range(row-(val-1), row+(val), 1):
            if(j<0 or j>=H):
                continue
            else:
                value = ret_map[j][col]
                if(value==0):
                    continue
                elif(value==1):
                    ret_map[j][col]=0
                else:
                    if([j, col] not in q and [j, col] not in visited):
                        q.append([j, col])
    
    for i in visited:
        ret_map[i[0]][i[1]] = 0

    print("visited", visited)
    v_2 = visited

    while(v_2):
        i = v_2[0]
        j = v_2[1]

    r_len = len(r)
    for j in range(W):
        for i in range(max(r), r_len-1, -1):
            ret_map[i][j] = ret_map[i-r_len][j]

    for i in range(r_len):
        for j in range(W):
            ret_map[i][j] = 0

    return ret_map

def solution(myMap, N):
    mymap = myMap.copy()
    answer = 0
    W = len(mymap[0])
    H = len(mymap)
    N = N

    minimum = W*H

    print("origin map: ", myMap)
    q = [[4, 5], [3, 4], [4, 4]]

    while(N>0):
        print("\n\n")
        mymap = reCreateMap(mymap, [q[0][0], q[0][1]])
        print("{} map: {}".format(4-N, mymap))

        q.pop(0)
        temp = countingNotZero(mymap)
        if(temp<minimum):
            minimum=temp
        N -= 1

    return minimum

T = int(input())

for i in range(T):
    N, W, H = map(int, input().split())
    myMap = [0 for _ in range(H)]
    for j in range(H):
        myMap[j] = list(map(int, input().split()))
    answer = solution(myMap, N)
    print("#{} {}".format(i+1, answer))