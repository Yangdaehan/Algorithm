def solution(sizes):
    answer = 0
    big1 = 0
    big2 = 0
    for i in range (len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            if big1 < sizes[i][1]:
                big1 = sizes[i][1]
            if big2 < sizes[i][0]:
                big2 = sizes[i][0]
        else :
            if big1 < sizes[i][0]:
                big1 = sizes[i][0]
            if big2 < sizes[i][1]:
                big2 = sizes[i][1]
        #print(big1, big2)
        
    answer = big1 * big2
    return answer