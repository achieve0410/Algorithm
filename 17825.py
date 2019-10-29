# supMap = [[2, 4, 6, 8, 10], [12, 14, 16, 18, 20], [22, 24, 26, 28, 30], [25, 30, 35], [40]]
Map = [[2, 4, 6, 8, 10, 13, 16, 19, 25, 30, 35, 40],
       [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30, 35, 40],
       [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 27, 26, 25, 30, 35, 40],
       [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]]
score = 0

def checkMap(player):
    map_num = player[0]
    location = player[1]

    if(map_num)==0:
        dd
    elif(map_num)==1:
        dd
    elif(map_num)==2:
        dd
    elif(map_num)==3:
        dd
    else:
        print("wrong map number")


def solution(dice_num, player):
    ## [map_num, location, score]
    players = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for player in players:
        checkMap(player)


if(__name__=='__main__'):
    inst = list(map(int, input().split()))

    for d_num in inst:
        solution(d_num, player)
    print(Map[0])
