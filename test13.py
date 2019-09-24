import sys

def findLength(x):
    return len(x)

def calcTypeNum(X):

    result = 0
    N = len(X)-1
    for i, x in enumerate(X):
        len_x = findLength(str(x))
        
        if(i==0):
            result += 2*(N)-1
        elif(x != 0):
            if(i==len(X)-1):
                result += len_x + 1
            else:
                result += len_x + 1
    return result+1

def main():
    N = int(sys.stdin.readline())
    X = [0 for i in range(N+1)]

    X_str = sys.stdin.readline().split()

    for i in range(N+1):
        X[i] = int(X_str[i])

    result = calcTypeNum(X)
    print(result)

if(__name__ == '__main__'):
    main()