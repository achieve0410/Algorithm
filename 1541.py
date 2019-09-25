import sys

def solution(question):

    Q = question

    Sum = 0
    plus = 1
    s_idx = 0
    e_idx = 1
    temp_num = 0

    for i in range(len(Q)):
        # print("i={}".format(i))
        # print("{}, {}, {}".format(s_idx, e_idx, Q[s_idx:e_idx]))

        if( plus==1 ): ## plus
            if( Q[i]=="+" ):
                temp_num += int(Q[s_idx:e_idx])
                s_idx = i+1
                e_idx = i+2
                continue
            elif( Q[i]=='-' ):
                temp_num += int(Q[s_idx:e_idx])
                Sum += temp_num
                temp_num = 0
                plus = 0
                s_idx = i+1
                e_idx = i+2
                continue
            else: ## number ( 0~9 )
                e_idx = i+1
                if(i==len(Q)-1):
                    temp_num += int(Q[s_idx:e_idx])
                    Sum += temp_num
                continue

        else: ## minus
            if( Q[i]=="+" ):
                temp_num += int(Q[s_idx:e_idx])
                s_idx = i+1
                e_idx = i+2
                continue
            elif( Q[i]=='-' ):
                temp_num += int(Q[s_idx:e_idx])
                Sum -= temp_num
                temp_num = 0
                s_idx = i+1
                e_idx = i+2
                continue
            else: ## number ( 0~9 )
                e_idx = i+1
                if(i==len(Q)-1):
                    temp_num += int(Q[s_idx:e_idx])
                    Sum -= temp_num
                continue

    return Sum

def main():

    question = sys.stdin.readline()

    result = solution(question)
    print(result)


if( __name__ == '__main__' ):
    main()