# Lab 3: Machine learning

def transpose(matrix):       # returns new matrix where the matrix row turns into column and vice versa
    M = matrix
    rows = len(M)              # nr of rown
    if rows == 0:
        return []
    cols = len(M[0])           # nr of columns
    new_m = []

    for i in range(cols):
        new_m.append([None] * rows)

    for i in range(rows):
        for j in range(cols):
            new_m[j][i] = M[i][j]
    return new_m


def powers(list, int1, int2):
    rows = len(list)
    cols = len(range(int1, int2 + 1))
    matrix = []
    for i in list:
        new_row = []
        for j in range(int1, int2 + 1):
            new = i**j
            new_row.append(new)
        matrix.append(new_row)
    return matrix


def matmul(A, B):          # multiply two matrices C = A * B
    rows = len(A)
    if rows == 0:
        return []
    cols = len(B[0])
    C = []

    for i in range(rows):
        C.append([0] * cols)

    for i in range(rows):
        for j in range(cols):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C


def invert(A):              # invert a square matrix
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    invert = [[A[1][1], -A[0][1]], 
              [-A[1][0], A[0][0]]]

    rows = len(invert)
    cols = len(invert[0])

    for i in range(rows):
        for j in range(cols):
            invert[i][j] *= 1/det
    return invert


def loadtxt(filename):
    inp_file = open(filename)
    matrix = []
    
    for line in inp_file:
        num_txt = line.split()
        row = []
    
        for element in num_txt:
            row.append(float(element))
        matrix.append(row)

    inp_file.close()
    return matrix
            


    

    
        