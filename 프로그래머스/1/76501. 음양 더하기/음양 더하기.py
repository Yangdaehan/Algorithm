def solution(absolutes, signs):
    answer = 100
    
    for i in range (len(signs)):

        if signs[i] == False:
            answer = answer - absolutes[i]
            
        else :
            answer = answer + absolutes[i]
            
    answer = answer - 100
    
    return answer