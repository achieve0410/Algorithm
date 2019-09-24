import sys

def checkP(P, Q):
    if( sorted(P) == list(set(sorted(Q)))):
        return True
    else:
        return False

def makeChild(P):
    Child = [0 for i in range(len(P))]

    for i in range(len(P)):
        if( i==0 ):
            Child[i] = 0
        else:
            Child[i] = P[Child[i-1]]
    return Child

def calcDiff(P):

    Q = P.copy()

    diff = 0
    temp = 0

    while( True ):
        print("P, Q : ", P, Q)
        zero_idx = Q.index(0)
        if( checkP(Q, makeChild(Q)) == True ):
            break

        for idx, q in enumerate(Q):
                if(idx == q):
                    temp = Q[idx]
                    Q[idx] = Q[0]
                    Q[0] = temp
                else:
                    continue

        if( Q[0] == 0):
            # print("zero is not the start")
            temp = Q[0]
            Q[0] = Q[-1]
            Q[-1] = temp

        ## 0은 제일 마지막일 수 없음
        elif( Q[-1] == 0 ):
            # print("zero is not the end")
            temp = Q[0]
            Q[0] = Q[-1]
            Q[-1] = temp

        ## 첫 요소는 최대값일 수 없음
        elif( Q[0] == len(Q)-1 ):
            # print("big one is not the start")
            temp = Q[-2]
            Q[-2] = Q[0]
            Q[0] = temp

        ## 0의 index가 제일 마지막 요소여야 함
        elif( Q[-1] != zero_idx ):
            # print("zero's index is the end")
            temp_idx = Q[-1]
            # print("temp_idx", temp_idx)
            ## 0의 index를 가지고 있는 값의 위치에 교체함
            temp = Q[temp_idx]
            Q[temp_idx] = Q[zero_idx]
            Q[zero_idx] = temp
            

    for i in range(len(P)):
        if(P[i] != Q[i]):
            diff += 1
    



    return diff

def main():
    N = int(sys.stdin.readline())

    P_str = sys.stdin.readline().split()
    P = []

    for i in range(N):
        p = int(P_str[i])
        P.append(p)
    
    result = calcDiff(P)
    print(result)

if(__name__ == '__main__'):
    main()