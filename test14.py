import sys

def checkFunc():
    return

def solution(M):
    M = M.copy()
    n = len(M)

    





    return



def main():

    k = int(sys.stdin.readline())

    for j in range(k):

        n = int(sys.stdin.readline())
        M = [[0]*n for i in range(n)]

        for i in range(n):
            M[i][0:n-1] = map(int, sys.stdin.readline().split())
        result = solution(M)
        print("#{} {}".format(j+1, result))

    return

if( __name__ == '__main__' ):
    main()