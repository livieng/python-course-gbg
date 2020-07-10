# Detta är ett program som beräknar factorials.

def main():
    n=int(input("Bestäm ett heltal: "))
    fact=1
    for factor in range(n,1,-1):
        fact=float(fact*factor)
    print("Factorial av", n, "är", fact)
main()
