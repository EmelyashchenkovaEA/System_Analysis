import numpy as np
import json

def task(str):

    e = 0.001
    mtr = np.array(json.loads(str))
    mtr =mtr.T

    matrix1= [[0 for i in range(3)] for i in range(3)]
    matrix2 = [[0 for i in range(3)] for i in range(3)]
    matrix3 = [[0 for i in range(3)] for i in range(3)]

    for i in range(len(mtr)):
        for j in range(len(mtr)):
            if mtr[i][0]<mtr[j][0]:
                matrix1[i][j]=1
            elif mtr[i][0]==mtr[j][0]:
                matrix1[i][j]=0.5
            else:
                matrix1[i][j]=0

    for i in range(len(mtr)):
        for j in range(len(mtr)):
            if mtr[i][1]<mtr[j][1]:
                matrix2[i][j]=1
            elif mtr[i][1]==mtr[j][1]:
                matrix2[i][j]=0.5
            else:
                matrix2[i][j]=0

    for i in range(len(mtr)):
        for j in range(len(mtr)):
            if mtr[i][2]<mtr[j][2]:
                matrix3[i][j]=1
            elif mtr[i][2]==mtr[j][2]:
                matrix3[i][j]=0.5
            else:
                matrix3[i][j]=0

    x= [[0 for i in range(3)] for i in range(3)]
    for i in range(len(mtr)):
        for j in range(len(mtr)):
            x[i][j]=(matrix1[i][j]+matrix2[i][j]+matrix3[i][j])/3


    k1 = np.array([1 / 3, 1 / 3, 1 / 3])
    k0 = np.array([1,1,1])

    while max(abs(np.array(k1)- np.array(k0)))>e:
        k0 = k1
        y = np.dot(x,k0)
        layambda = np.dot([1,1,1],y)
        k1 = 1/layambda*y
    out = [round(i,3) for i in k1]
    return out
