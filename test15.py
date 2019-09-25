import sys

def main():

    n = map(int, sys.stdin.readline())

    arr = [6,5,3,4,2,1]

    for i in range(len(arr)):
        # print("arr[{}] : {}".format(i, arr[i]))
        if( i%2==0 ):
            if( i!=0 ):
                print("{}'s parent is {}".format(arr[i], arr[int(i/2-1)]))
            else:
                print("{} is root node".format(arr[i]))

        else:
                print("{}'s parent is {}".format(arr[i], arr[int(i/2)]))

    return

if( __name__ == '__main__' ):
    main()