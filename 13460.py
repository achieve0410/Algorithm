import copy

board = []
visited = set()
Min = 11

def bfs(board, red, blue, visited, count):
    global Min

    brd = copy.deepcopy(board)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited.add(red)
    # print(red, blue, visited, count)

    for i in range(4):
        for o in brd:
            print(o)
        print("\n\n")
    
        rfin = 0
        bfin = 0
        rx, ry, bx, by = red[0], red[1], blue[0], blue[1]

        ## red
        rcnt = 1
        bcnt = 1
        while(True):

            ## red
            rx = red[0] + rcnt * dx[i]
            ry = red[1] + rcnt * dy[i]

            if(rx!=bx or ry!=by):
                if(brd[rx][ry]=='.' or brd[rx][ry]=='B'):
                    rcnt += 1
                elif(brd[rx][ry]=='O'):
                    rfin = 1
                    rcnt += 1
                else:
                    rx -= dx[i]
                    ry -= dy[i]
                    break
            else:
                rx -= dx[i]
                ry -= dy[i]
                break

            ## blue
            bx = blue[0] + bcnt * dx[i]
            by = blue[1] + bcnt * dy[i]

            if(bx!=rx or by!=ry):
                if(brd[bx][by]=='.' or brd[bx][by]=='R'):
                    bcnt += 1
                elif(brd[bx][by]=='O'):
                    bfin = 1
                    break
                else:
                    bx -= dx[i]
                    by -= dy[i]
                    break
            else:
                bx -= dx[i]
                by -= dy[i]
                break

        # print("rx, ry: {}, {}".format(rx, ry))

        ## blue
        # bcnt = 1
        # while(True):
        #     bx = blue[0] + bcnt * dx[i]
        #     by = blue[1] + bcnt * dy[i]

        #     if(bx!=rx or by!=ry):
        #         if(brd[bx][by]=='.' or brd[bx][by]=='R'):
        #             bcnt += 1
        #         elif(brd[bx][by]=='O'):
        #             bfin = 1
        #             break
        #         else:
        #             bx -= dx[i]
        #             by -= dy[i]
        #             break
        #     else:
        #         bx -= dx[i]
        #         by -= dy[i]
        #         break

        brd[red[0]] = brd[red[0]][:red[1]] + '.' + brd[red[0]][red[1]+1:M]
        brd[blue[0]] = brd[blue[0]][:blue[1]] + '.' + brd[blue[0]][blue[1]+1:M]        
        brd[rx] = brd[rx][:ry] + 'R' + brd[rx][ry+1:M]
        brd[bx] = brd[bx][:by] + 'B' + brd[bx][by+1:M]

        # print("bx, by: {}, {}".format(bx, by))
        # print("rfin, bfin: {}, {}".format(rfin, bfin))
        
        if(rfin==1 and bfin==0):
            if(Min>count):
                Min = count
        if(bfin==1):
            continue

        ## bfs
        # if(board[rx][ry]=='.' or board[rx][ry]=='O'):
        if((rx, ry) not in visited):
            if(count<=10):
                vst = copy.deepcopy(visited)
                bfs(brd, (rx, ry), (bx, by), vst, count+1)

def solution(board):

    ## find R, B ball
    for i in range(1, N-1, 1):
        for j in range(1, M-1, 1):
            if(board[i][j]=='R'):
                red = (i, j)
            elif(board[i][j]=='B'):
                blue = (i, j)
    
    ## dfs
    bfs(board, red, blue, visited, 1)
    if(Min==11):
        print(-1)
    else:
        print(Min)

    ## dfs
    bfs(board, blue, red, visited, 1)
    if(Min==11):
        print(-1)
    else:
        print(Min)



if(__name__ == '__main__'):
    N, M = map(int, input().split())

    for i in range(N):
        board.append(input())
    # print(board)
    solution(board)