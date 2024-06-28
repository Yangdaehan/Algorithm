def solution(food):
    nfoods = [f//2 for f in food[1:]]
    nfoods_str = ''.join([str(food) * nfood for food, nfood in enumerate(nfoods, 1)])
    return nfoods_str + '0' + nfoods_str[::-1]