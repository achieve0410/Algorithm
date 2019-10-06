import sys

def solution_n(picture):
    answer = 0
    visited = []

    rows = len(picture)
    cols = len(picture[0])

    for row in range(rows):
        for col in range(cols):
            curr = [row, col]

            if(curr in visited):
                continue
            else:
                answer += 1
                q = []
                q.append(curr)

                while(q):
                    temp_curr = q.pop(0)
                    visited.append(temp_curr)

                    temp_i = temp_curr[0]
                    temp_j = temp_curr[1]

                    temp_val = picture[temp_i][temp_j]

                    for l_idx in range(temp_j-1, -1, -1):
                        if( picture[temp_i][l_idx]!=temp_val ):
                            break
                        else:
                            if( [temp_i, l_idx] not in visited ):
                                if( [temp_i, l_idx] not in q ):
                                    q.append([temp_i, l_idx])

                    for r_idx in range(temp_j+1, cols, 1):
                        if( picture[temp_i][r_idx]!=temp_val ):
                            break
                        else:
                            if( [temp_i, r_idx] not in visited ):
                                if( [temp_i, r_idx] not in q ):
                                    q.append([temp_i, r_idx])

                    for u_idx in range(temp_i-1, -1, -1):
                        if( picture[u_idx][temp_j]!=temp_val ):
                            break
                        else:
                            if( [u_idx, temp_j] not in visited ):
                                if( [u_idx, temp_j] not in q ):
                                    q.append([u_idx, temp_j])

                    for d_idx in range(temp_i+1, rows, 1):
                        if( picture[d_idx][temp_j]!=temp_val ):
                            break
                        else:
                            if( [d_idx, temp_j] not in visited ):
                                if( [d_idx, temp_j] not in q ):
                                    q.append([d_idx, temp_j])
    return answer

def solution_r(picture):
    answer = 0
    visited = []

    rows = len(picture)
    cols = len(picture[0])

    for row in range(rows):
        for col in range(cols):
            curr = [row, col]

            if(curr in visited):
                continue
            else:
                answer += 1
                q = []
                q.append(curr)

                temp_val = picture[curr[0]][curr[1]]

                if(temp_val=='B'):
                    temp_var = 0
                else:
                    temp_var = 1

                while(q):
                    temp_curr = q.pop(0)
                    visited.append(temp_curr)

                    temp_i = temp_curr[0]
                    temp_j = temp_curr[1]

                    for l_idx in range(temp_j-1, -1, -1):
                        if( temp_var==0 ):
                            if( picture[temp_i][l_idx]!=temp_val ):
                                break
                        elif( temp_var==1 ):
                            if( picture[temp_i][l_idx]=='B' ):
                                break
                        if( [temp_i, l_idx] not in visited ):
                            if( [temp_i, l_idx] not in q ):
                                q.append([temp_i, l_idx])

                    for r_idx in range(temp_j+1, cols, 1):
                        if( temp_var==0 ):
                            if( picture[temp_i][r_idx]!=temp_val ):
                                break
                        elif( temp_var==1 ):
                            if( picture[temp_i][r_idx]=='B' ):
                                break
                        if( [temp_i, r_idx] not in visited ):
                            if( [temp_i, r_idx] not in q ):
                                q.append([temp_i, r_idx])

                    for u_idx in range(temp_i-1, -1, -1):
                        if( temp_var==0 ):
                            if( picture[u_idx][temp_j]!=temp_val ):
                                break
                        elif( temp_var==1 ):
                            if( picture[u_idx][temp_j]=='B' ):
                                break
                        if( [u_idx, temp_j] not in visited ):
                            if( [u_idx, temp_j] not in q ):
                                q.append([u_idx, temp_j])

                    for d_idx in range(temp_i+1, rows, 1):
                        if( temp_var==0 ):                            
                            if( picture[d_idx][temp_j]!=temp_val ):
                                break
                        elif( temp_var==1 ):                            
                            if( picture[d_idx][temp_j]=='B' ):
                                break
                        if( [d_idx, temp_j] not in visited ):
                            if( [d_idx, temp_j] not in q ):
                                q.append([d_idx, temp_j])
    return answer

N = int(sys.stdin.readline())

picture = [[""]*N for i in range(N)]

for rep in range(N):
    for idx, row in enumerate(sys.stdin.readline()):
        if(idx!=N):
            picture[rep][idx] = row

answer_n = solution_n(picture)
answer_r = solution_r(picture)

print(answer_n, answer_r)