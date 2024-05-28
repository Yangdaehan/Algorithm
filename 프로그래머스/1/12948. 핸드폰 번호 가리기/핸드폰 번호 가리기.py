def solution(phone_number):
    answer = ''
    a = len(phone_number)
    answer = '*'*(a-4) + phone_number[-4:a]
    
    return answer