# Lab 3: Machine learning - main program:
from matrix import *
import matplotlib.pyplot as plt
import sys

def main():
    filename = str(sys.argv[1])
    matrix = loadtxt(filename)
    M = transpose(matrix)
    X = M[0]
    Y = M[1]
    Xp  = powers(X,0,1)
    Yp  = powers(Y,1,1)
    Xpt = transpose(Xp)

    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    Y2 = []
    for x in X:
        Y2.append(b + m * x)

    plt.plot(X,Y2)      # line
    plt.plot(X,Y,'ro')  # dots
    plt.show()

main() 