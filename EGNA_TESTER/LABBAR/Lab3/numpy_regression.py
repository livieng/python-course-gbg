# Lab 3: Machine learning - main program:
from numpy import *
import matplotlib.pyplot as plt
import sys

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
    M = array(matrix)
    return M

def main():
    filename = str(sys.argv[1])
    matrix = loadtxt(filename)
    n = int(sys.argv[2])
    M = transpose(matrix)
    X = M[0]
    Y = M[1]
    Xp  = powers(X,0,n)
    Yp  = powers(Y,1,1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]

    X2 = linspace(min(X), max(X),int((max(X)-min(X))/0.2)).tolist()

    Y2 = []
    for x in X2:
        Y2.append(poly(a,x))

    plt.plot(X2,Y2)     # regression
    plt.plot(X,Y,'ro')  # dots
    plt.show()

def poly(a,x):
    y = 0
    power = 0
    for i in a:
        y += i * x**power
        power += 1
    return y

if __name__ == "__main__":
    main()  
