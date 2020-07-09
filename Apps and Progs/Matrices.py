import numpy as np;

def Problem1():
    A = [[1,-2,3],
        [4,5,-6]]
    B = [[3,0,2],
        [-7,1,8]]
    result = [[0, 0, 0],
              [0, 0, 0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    for r in result:
        print(r)

    print(2*A-B)

    print(3*B)


def Problem2():
    A = [[1,3],
        [2,-1]]
    B = [[2,0,-4],
         [3,-2,6]]
    result = [[0, 0, 0],
              [0, 0, 0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    for r in result:
        print(r)

    print(B*A)

def Problem3():
    A = [[1, 0, 2],
         [2, -1, 3],
         [4,1,8]]
    B = [[-11, 2, 2],
         [-4, 0, 1],
         [6,-1,-1]]
    result = [[0, 0, 0],
              [0, 0, 0],
               [0, 0, 0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    for r in result:
        print(r)

    print(B*A)

def Problem4():
    A = [[7,5,-3],
         [3,-5,2],
         [5,3,-7]]
    B = [[16],
        [-8],
         [0]]
    X = [[x],
         [y],
         [z]]
    print(solve(X))
    print(A*X,"=",B)
    print(1/A)
    print((1/A)*X,"=",B)

def Problem5():
    A = [[2,-1,5,1],
         [3,2,2,-6],
         [1,3,3,-1],
         [5,-2,-3,3]]
    B = [[-3],
        [-32],
         [47],
         [49]]
    X = [[w],
        [x],
         [y],
         [z]]
    print(solve(X))
    print(A*X,"=",B)
    print(1/A)
    print((1/A)*X,"=",B)