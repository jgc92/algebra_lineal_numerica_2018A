from math import sqrt

def transpose(A):
    B = []
    l = len(A)
    c = len(A[0])

    if c == 1:

        # A is a vector

        for i in range(c):
            B.append([])
            for j in range(l):
                B[i].append(A[j])
    else:
        for i in range(c):
            B.append([])
            for j in range(l):
                B[i].append(A[j][i])

    return B


def getL(A):

    lines = len(A)
    columns = len(A[0])

    L = [[0 for j in range(columns)] for i in range(lines)]

    L[0][0] = sqrt(A[0][0])
    for i in range(1, lines, 1):
        L[i][0] = 1 / float(L[0][0]) * A[i][0]

    for i in L:
        print(i)
    print("\n")

    for i in range(1, lines, 1):
        acc = 0
        for j in range(i):
            if j == 0:
                acc = L[i][j] ** 2
            else:
                acc = acc - L[i][j] ** 2
        L[i][i] = sqrt(A[i][i] - acc)
        
        if i + 1 == lines:
            L[i][i] = 1.
            return L

        acc = 0
        for k in range(i):
            if k == 0:
                acc = L[i + 1][k] * L[i][k]
            else:
                acc = acc - L[i + 1][k] * L[i][k]

        L[i + 1][i] = 1 / float(L[i][i]) * (A[i + 1][i] - acc)



			
