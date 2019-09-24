import operator

def solution(DNA, N, M):

    resultString = ''
    resultDistance = 0
    for i in range(M):
        myDic = {}
        mystring = 'Z'
        mydistance = 0
        for j in range(N):
            if( DNA[j][i] not in myDic ):
                myDic[DNA[j][i]] = 1
            else:
                myDic[DNA[j][i]] += 1

            if(myDic[DNA[j][i]] >= mydistance):
                mydistance = myDic[DNA[j][i]]
                if( ord(mystring) - ord(DNA[j][i]) > 0 ):
                    mystring = DNA[j][i]
            
        resultString += mystring
        resultDistance += (N - mydistance)
        
    return resultString, resultDistance

def main():

    N, M = input().split()
    N = int(N)
    M = int(M)

    DNA = []

    for i in range(N):
        dna = input()
        DNA.append(dna)

    s_result, n_result = solution(DNA, N, M)

    print(s_result)
    print(n_result)

if( __name__ == '__main__'):
    main()