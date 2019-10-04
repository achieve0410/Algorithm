import sys

def solution(farm):
    sheep, wolf = 0, 0

    visited = []

    row = len(farm)
    col = len(farm[0])

    for i in range(1, row-1, 1):
        for j in range(1, col-1, 1):
            curr = [i, j]
            # print("curr: {}".format(curr))
            if(farm[i][j]=='#'):
                # print("#\n")
                continue
            elif(curr in visited):
                # print("visited\n")
                continue
            else:
                # print("else\n")
                myqueue = []
                tmp_s, tmp_w = 0, 0

                myqueue.append(curr)
                while(myqueue):
                    tmp_curr = myqueue.pop(0)
                    tmp_i = tmp_curr[0]
                    tmp_j = tmp_curr[1]

                    if(farm[tmp_i][tmp_j]=='k'):
                        tmp_s+=1
                    elif(farm[tmp_i][tmp_j]=='v'):
                        tmp_w+=1

                    if(tmp_curr not in visited):
                        visited.append(tmp_curr)

                    ## left
                    for idx in range(tmp_j-1, 0, -1):
                        # print("\tidx in left: {}".format(idx))
                        if(farm[tmp_i][idx]=='#'):
                            break
                        else:
                            if([tmp_i, idx] not in visited):
                                if([tmp_i, idx] not in myqueue):
                                    # print("\t\t left\n")
                                    myqueue.append([tmp_i, idx])
                                else:
                                    break
                            else:
                                break

                    ## right
                    for idx in range(tmp_j+1, col-1, 1):
                        # print("\tidx in right: {}".format(idx))
                        if(farm[tmp_i][idx]=='#'):
                            break
                        else:
                            if([tmp_i, idx] not in visited):
                                if([tmp_i, idx] not in myqueue):
                                    # print("\t\t right\n")
                                    myqueue.append([tmp_i, idx])
                                else:
                                    break
                            else:
                                break

                    ## up
                    for idx in range(tmp_i-1, 0, -1):
                        # print("\tidx in up: {}".format(idx))
                        if(farm[idx][tmp_j]=='#'):
                            break
                        else:
                            if([idx, tmp_j] not in visited):
                                if([idx, tmp_j] not in myqueue):
                                    # print("\t\t up\n")
                                    myqueue.append([idx, tmp_j])
                                else:
                                    break
                            else:
                                break

                    ## down
                    for idx in range(tmp_i+1, row-1, 1):
                        # print("\tidx in down: {}".format(idx))
                        if(farm[idx][tmp_j]=='#'):
                            break
                        else:
                            if([idx, tmp_j] not in visited):
                                if([idx, tmp_j] not in myqueue):
                                    # print("\t\t down\n")
                                    myqueue.append([idx, tmp_j])
                                else:
                                    break
                            else:
                                break
                if(tmp_s>tmp_w):
                    sheep+=tmp_s
                else:
                    wolf+=tmp_w

    return sheep, wolf

R, C = map(int, sys.stdin.readline().split())
farm = []

for i in range(R):
    farm += list(sys.stdin.readline().split())

sheep, wolf = solution(farm)
print(sheep, wolf)