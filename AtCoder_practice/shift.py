#https://atcoder.jp/contests/abs/tasks/abc081_b
import sys

sys.setrecursionlimit(1000000)
N = int(input())
q = lambda n:n//2
mod = lambda n:n%2

A_arr = list(map(int,input().split()))

def return_q(arr,count=0):

    mod_arr = list(map(mod,arr))

    if 1 not in mod_arr:
        arr = list(map(q,arr))
        count +=1
        arr,count =  return_q(arr,count)
    return arr,count
arr,count = return_q(A_arr,count=0)
print(count)