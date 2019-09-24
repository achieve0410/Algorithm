
def findHeight(N, arr):

    line = [ 0*N for i in range(N) ]
    count = 0

    while( count<N ):
        tempCount = 0
        for idx, i in enumerate(arr):
            if( tempCount != arr[count] ):
                if( line[idx] == 0 ):
                    tempCount += 1
                else:
                    continue
            else:
                if( line[idx] == 0 ):
                    line[idx] = count+1
                    break
                else:
                    continue
        count += 1
    return line

def printlist(line):
    string = ''

    for i, _ in enumerate(line):
        string += str(line[i])
        if( i!=len(line)-1 ):
            string += " "
    return string

def main():

    N = input()
    N = int(N)
    arr = []

    n_str = input().split()

    for i in range(N):
        n = int(n_str[i])
        arr.append(n)

    result = printlist(findHeight(N, arr))
    print(result)

if (__name__ == '__main__'):
    main()