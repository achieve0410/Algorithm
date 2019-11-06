

def solution(cmd):
    ans = [1, 0, 1, 0, 0, 1]
    char = set()

    for i in range(6):
        
        ## more than 2
        char.add(cmd[i])
        if(len(char)>2):
            return 0
        
        ## compare
        if(cmd[i]==cmd[i+1]):
            temp = 1
        else:
            temp = 0
        
        if(temp!=ans[i]):
            return 0
    return 1

if(__name__=='__main__'):
    T = int(input())
    
    for i in range(T):
        cmd = input()
    
        if(len(cmd)!=7):
            answer = 0
            print(answer)
        
        else: ## len(cmd)==7
            answer = solution(cmd)
            print(answer)