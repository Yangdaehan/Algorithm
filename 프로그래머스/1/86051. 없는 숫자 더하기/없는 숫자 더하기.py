def solution(numbers):
    answer = 0
    
    for i in range(10):
        if i not in numbers:
            answer = answer + i
            print(i)
    
    return answer