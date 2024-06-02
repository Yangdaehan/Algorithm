def solution(price, money, count):
    answer = -1
    
    tot_pri = 0
    for i in range (count):
        tot_pri = price * (i+1) + tot_pri
        print(tot_pri)
    answer = tot_pri - money
    
    if (answer < 0 ):
        answer = 0

    return answer