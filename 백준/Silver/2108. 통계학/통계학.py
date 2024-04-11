import sys

n = int(input())
x=[]
for i in range (n):
    x.append(int(sys.stdin.readline()))


x.sort()
y = sum(x)

# 산술평균
print(round(y/n))

# 중앙값
print(x[n//2])

# 최빈값
dic = dict()
for i in x:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

mx = max(dic.values())  # 빈도수 중 최대값 구하기
mx_dic = []  # 최빈값 숫자를 저장할 배열

for i in dic:
    if mx == dic[i]:
        mx_dic.append(i)

if len(mx_dic) > 1: # 빈도수 많은게 여러개일 때
    print(mx_dic[1])
else:
    print(mx_dic[0])


#범위
print(max(x) - min(x)) 

