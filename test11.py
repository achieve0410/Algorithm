import sys

def dvdChoco(K):

    repOfChoco = 0

    temp_K = K
    count = 0
    while(temp_K>1):
        count += 1
        temp_K /= 2

    scaleOfChoco = 2**count

    if(K == scaleOfChoco):
        return scaleOfChoco, repOfChoco
    else:
        temp_sum = 0
        temp_scale = scaleOfChoco
        while( True ):
            if( temp_sum == K ):
                break
            temp_scale /= 2
            pieceOfChoco = temp_scale
            if(temp_sum+pieceOfChoco>K):
                repOfChoco += 1
                continue
            temp_sum += pieceOfChoco
            repOfChoco += 1

    return scaleOfChoco, repOfChoco

def main():

    K = int(sys.stdin.readline())

    scale, count = dvdChoco(K)
    print(scale, count)

if( __name__ == '__main__'):
    main()