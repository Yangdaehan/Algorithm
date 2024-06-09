def solution(arr):
    x=9998989989989898989898898989898989
    y=[]
    for i in range(len(arr)):
        if arr[i] != x:
            y.append(arr[i])
            x = arr[i]
        
    return y