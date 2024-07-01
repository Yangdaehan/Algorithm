def solution(strings, n):
    answer = []
    n_keyword = [] 
    strings.sort() 
    
    for i in strings:
        keyword = i[n]
        n_keyword.append(keyword)
    
    n_keyword.sort()
    
    for i in n_keyword:
        for j in strings:
            if i == j[n] and j not in answer:
                answer.append(j)
    
    return answer