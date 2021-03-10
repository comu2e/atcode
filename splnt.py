# https://atcoder.jp/contests/past202005-open/tasks/past202005_e

N,M,Q = map(int,input().split())

graph = [[False for i in range(0,N)] for i in range(0,N)]
for i in range(0,M):
    u,v = map(int,input().split())
    # 頂点番号はすべて-1する
    u -= 1
    v -= 1
    # uとvの間に辺があるため
    graph[u][v] = True
    graph[v][u] = True

c_arr = list(map(int,input().split()))

for i in range(0,Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        x = query[1]

        x -= 1

        # 頂点xの色を出力する
        print(c_arr[x])

        for i in range(0,N):
            if graph[x][i]:
                c_arr[i] = c_arr[x]

    if(query[0] == 2):
        x = query[1]
        y = query[2]

        x -= 1

        print(c_arr[x])

        c_arr[x] = y

