
def calcMinTime(P):
    h_list = P
    totalMin = 0
    exeMin = 0

    while h_list:
        tempMin = min(h_list)
        exeMin += tempMin
        totalMin += exeMin
        h_list.remove(tempMin)

    return totalMin

def main():
    
    N = int(input())
    P_str = input().split()
    P = []

    for i in range(N):
        p = int(P_str[i])
        P.append(p)
    
    result = calcMinTime(P)
    print(result)

if( __name__ == '__main__'):
    main()