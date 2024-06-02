def solution(a, b):
    sum =0
    for i in range (len(a)):
        tmp = a[i]*b[i]
        sum +=tmp
    return sum