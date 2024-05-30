def solution(s):
    b=len(s)
    a=int(len(s)/2)
    if b%2==0:
        return s[a-1]+s[a]
    else :
        return s[a]
