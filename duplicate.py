N = int(input())
arr = []
for i in range(0,N):
    arr.append(int(input()))

solve_arr = []
for i in range(0,N):
    for num in arr:
       if arr[i] == num:
           solve_arr.append(num)
       else:
           pass
print(solve_arr)