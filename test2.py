
def calcCoin(coin, cost):
    mycoin = coin
    mycost = cost
    count = 0

    while ( mycost>0 ):
        for i in range(len(mycoin)-1, -1, -1):
            if(mycost - mycoin[i] >= 0):
                num = int(mycost/mycoin[i])
                if(num>=2):
                    mycost = mycost - (mycoin[i] * num)
                    count += (num)
                    break
                else:
                    mycost -= mycoin[i]
                    count += 1
                    break
            else:
                continue

    return count

def main():

    N, K = input().split()
    N = int(N)
    K = int(K)
    A = []
    
    for i in range(N):
        a = int(input())
        A.append(a)
    
    result = calcCoin(A, K)

    print(result)

if( __name__ == '__main__'):
    main()