# detta program konverterar fahrenheit och celcius

# F = 9/5 * C + 32

def main():
    print("Detta program konverterar Fahrenheit till Calcius")
    F=eval(input("Ange grader i Fahrenheit: "))
    C=(5/9)*(F-32)
    print(F, "grader Fahrenheit är ", C, "grader Celcius.")
main()