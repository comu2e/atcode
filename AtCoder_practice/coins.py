#https://atcoder.jp/contests/abs/tasks/abc087_b
A = int(input())
B = int(input())
C = int(input())
X = int(input())
# X=50ｋ(1<=k<=400)
# C=k-(10A+2B)
# 1+9A+B<=k

k = X //50
a = A//50
b = B//50
c = C//50
count = 0
if a != 0:
    for i in range(1,a+1):
        for j in range(1,b+1):
            if (0<= j <= k-1-9*i):
                count +=1
else:
    for i in range(1,b+1):
        if (0<= i <= k-1):
            count +=1
print(count)

