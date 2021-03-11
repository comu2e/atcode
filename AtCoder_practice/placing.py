# https://atcoder.jp/contests/abs/tasks/abc081_a
s = (input())

s_arr = [i for i in s]

count = 0
for i in s_arr:
    if i == "1":
        count +=1

print(count)

