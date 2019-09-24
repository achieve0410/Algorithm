
def calcChange(coin, cost):

    mycoin = coin
    mycost = cost
    count = 0

    while( mycost ):
        for i in mycoin:
            if( mycost - i>=0 ):
                num = int(mycost/i)
                mycost -= i * num
                count += num
            else:
                continue
    return count

def main():
    coin = [500, 100, 50, 10, 5, 1]
    cost = int(input())

    result = calcChange(coin, 1000-cost)
    print(result)

    return

if( __name__ == '__main__'):
    main()