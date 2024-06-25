def solution(numbers):
    answer = []
    
    for i in range (0,len(numbers)-1,1):
        for j in range(i+1,len(numbers)):
            a = numbers[i]+numbers[j]
            if(a not in answer):
                answer.append(a)
        
    
    return sorted(answer)