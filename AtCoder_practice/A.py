# https://atcoder.jp/contests/practice2/tasks/practice2_a
from collections import deque

N, Q = map(int, input().split())
graph = [[False for i in range(0, N)] for i in range(0, N)]

for i in range(0, Q):
    t, u, v = list(map(int, input().split()))
    is_connect_arr = []
    if t == 0:
        graph[u][v] = True
        graph[v][u] = True
    elif t == 1:
        for j in range(N):
        #  連結していることを判定するアルゴリズム書く。幅探索？