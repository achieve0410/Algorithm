import sys

def solution(field):
    visited = []

    row = len(field)
    col = len(field[0])

    area = []
    count = 0

    for i in range(row):
        for j in range(col):
            curr = [i, j]
            if(field[i][j]==1):
                continue
            elif(curr in visited):
                continue
            else:
                cnt = 0
                count += 1
                myqueue = []

                myqueue.append(curr)
                while(myqueue):
                    tmp_curr = myqueue.pop(0)
                    cnt += 1
                    tmp_i = tmp_curr[0]
                    tmp_j = tmp_curr[1]

                    if(tmp_curr not in visited):
                        visited.append(tmp_curr)

                    ## left
                    for idx in range(tmp_j-1, -1, -1):
                        if(field[tmp_i][idx]==1):
                            break
                        else:
                            if([tmp_i, idx] not in visited):
                                if([tmp_i, idx] not in myqueue):
                                    myqueue.append([tmp_i, idx])
                                else:
                                    break
                            else:
                                break

                    ## right
                    for idx in range(tmp_j+1, col, 1):
                        if(field[tmp_i][idx]==1):
                            break
                        else:
                            if([tmp_i, idx] not in visited):
                                if([tmp_i, idx] not in myqueue):
                                    myqueue.append([tmp_i, idx])
                                else:
                                    break
                            else:
                                break

                    ## up
                    for idx in range(tmp_i-1, -1, -1):
                        if(field[idx][tmp_j]==1):
                            break
                        else:
                            if([idx, tmp_j] not in visited):
                                if([idx, tmp_j] not in myqueue):
                                    myqueue.append([idx, tmp_j])
                                else:
                                    break
                            else:
                                break

                    ## down
                    for idx in range(tmp_i+1, row, 1):
                        if(field[idx][tmp_j]==1):
                            break
                        else:
                            if([idx, tmp_j] not in visited):
                                if([idx, tmp_j] not in myqueue):
                                    myqueue.append([idx, tmp_j])
                                else:
                                    break
                            else:
                                break
                area.append(cnt)

    return count, sorted(area)

M, N, K = map(int, sys.stdin.readline().split())
field = [[0]*M for i in range(N)]

for i in range(K):
    mp = list(map(int, sys.stdin.readline().split()))
    for col in range(mp[1], mp[3], 1):
        for row in range(mp[0], mp[2], 1):
            field[row][col] = 1

answer = solution(field)

print(answer[0])
print(" ".join(map(str, answer[1])))