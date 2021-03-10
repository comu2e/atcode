N = int(input())
A_temp = 0
for i in range(0,N):
    if i == 0:
        A_temp = int(input())
    else:
        A_i = int(input())
        if A_i == A_temp:
            print('stay')
            A_temp = A_i
        elif A_i > A_temp:
            print("up {0}".format(A_i - A_temp))
            A_temp = A_i
        elif A_i < A_temp:
            print("down {0}".format(A_temp -A_i))
            A_temp = A_i
