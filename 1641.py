import sys

def solution(N, M, book):
    Book = book.copy()
    # pos_arr = []
    # neg_arr = []
    result = 0

    # for i in range(N):
    #     if(Book[i]>=0):
    #         pos_arr.append(Book[i])
    #     else:
    #         neg_arr.append(Book[i])

    pos_arr = [i for i in Book if(i>0)]
    neg_arr = [i for i in Book if(i<0)]

    pos_arr = list(map(abs, pos_arr))
    neg_arr = list(map(abs, neg_arr))

    ## 일방적인 배열에 대한 처리가 필요
    ## 전부 양수이거나, 전부 음수이거나

    if( len(neg_arr)==0 ): ## 전부 양수이면
        arr = pos_arr.copy()
        count = 0
        while(True):
            if( len(arr)==0 ):
                break            

            if( count==0 ):
                temp_max = max(arr)
                result += temp_max

                if( len(arr)<M ):   
                    for i in range(len(arr)):
                        temp_max = max(arr)
                        arr.remove(temp_max)
                else:
                    for i in range(M):
                        temp_max = max(arr)
                        arr.remove(temp_max)
                count += 1
            else:
                temp_max = max(arr)
                result += (temp_max*2)

                if( len(arr)<M ):   
                    for i in range(len(arr)):
                        temp_max = max(arr)
                        arr.remove(temp_max)
                else:
                    for i in range(M):
                        temp_max = max(arr)
                        arr.remove(temp_max)

    elif( len(pos_arr)==0 ): ## 전부 음수이면
        arr = neg_arr.copy()
        count = 0
        while(True):
            if( len(arr)==0 ):
                break            

            if( count ==0 ):
                temp_max = max(arr)
                result += temp_max

                if( len(arr)<M):   
                    for i in range(len(arr)):
                        temp_max = max(arr)
                        arr.remove(temp_max)
                else:
                    for i in range(M):
                        temp_max = max(arr)
                        arr.remove(temp_max)
                count += 1
            else:
                temp_max = max(arr)
                result += (temp_max*2)

                if( len(arr)<M):   
                    for i in range(len(arr)):
                        temp_max = max(arr)
                        arr.remove(temp_max)
                else:
                    for i in range(M):
                        temp_max = max(arr)
                        arr.remove(temp_max)



    elif( max(pos_arr) >= max(neg_arr) ): ## 양수가 더 클 경우
        
        ## 음수 배열 처리
        arr = neg_arr.copy()
        while(True):
            if( len(arr)==0 ):
                break
            temp_max = max(arr)
            result += (2*temp_max)

            if( len(arr)<M):
                for i in range(len(arr)):
                    temp_max = max(arr)
                    arr.remove(temp_max)
            else:
                for i in range(M):
                    temp_max = max(arr)
                    arr.remove(temp_max)

        ## 양수 배열 처리
        arr = pos_arr.copy()
        count = 0
        while(True):
            if( len(arr)==0 ):
                break            

            if( count ==0 ):
                temp_max = max(arr)
                result += temp_max

                if( len(arr)<M):   
                    for i in range(len(arr)):
                        temp_max = max(arr)
                        arr.remove(temp_max)
                else:
                    for i in range(M):
                        temp_max = max(arr)
                        arr.remove(temp_max)
                count += 1
            else:
                temp_max = max(arr)
                result += (temp_max*2)

                if( len(arr)<M):   
                    for i in range(len(arr)):
                        temp_max = max(arr)
                        arr.remove(temp_max)
                else:
                    for i in range(M):
                        temp_max = max(arr)
                        arr.remove(temp_max)

    else: ## 음수가 더 클 경우
        
        ## 양수 배열 처리
        arr = pos_arr.copy()
        while(True):
            if( len(arr)==0 ):
                break
            temp_max = max(arr)
            result += (2*temp_max)

            if( len(arr)<M):
                for i in range(len(arr)):
                    temp_max = max(arr)
                    arr.remove(temp_max)
            else:
                for i in range(M):
                    temp_max = max(arr)
                    arr.remove(temp_max)

        ## 음수 배열 처리
        arr = neg_arr.copy()
        count = 0
        while(True):
            if( len(arr)==0 ):
                break            

            if( count ==0 ):
                temp_max = max(arr)
                result += temp_max

                if( len(arr)<M):   
                    for i in range(len(arr)):
                        temp_max = max(arr)
                        arr.remove(temp_max)
                else:
                    for i in range(M):
                        temp_max = max(arr)
                        arr.remove(temp_max)
                count += 1
            else:
                temp_max = max(arr)
                result += (temp_max*2)

                if( len(arr)<M):   
                    for i in range(len(arr)):
                        temp_max = max(arr)
                        arr.remove(temp_max)
                else:
                    for i in range(M):
                        temp_max = max(arr)
                        arr.remove(temp_max)

    return result



def main():
    N, M = map(int, sys.stdin.readline().split())    
    book = list(map(int, sys.stdin.readline().split()))

    result = solution(N, M, book)
    print(result)

if( __name__ == '__main__' ):
    main()