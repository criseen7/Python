def Fibonacci_Recursion(n):
    if n <= 0:
        print (0)
    elif n == 1:
        print (1)
    print (Fibonacci_Recursion(n-1) + Fibonacci_Recursion(n-2))

def Fibonacci_DP(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = Fibonacci_DP(n-1, memo) + Fibonacci_DP(n-2,memo)
    return memo[n]

def Fibonacci_Iteration(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a,b = 0,1
    for i in range(2,n+1):
        a,b = b, a+b
    return b

def main():
    while True:
        try:
            option = int(input("Choose an option\n1.Use Recursion\n2.Use DP(Memoizacion)\n3.Use iteration\n4.Exit\nOption: "))
            n=int(input("Enter the number to calculate fibonacci series: "))
            if option == 1:
                print(Fibonacci_Recursion(n))
            elif option == 2:
                print(Fibonacci_DP(n))
            elif option == 3:
                print(Fibonacci_Iteration(n))
            elif option == 4:
                print("Exiting the program...")
                break
            else:
                print("Invalid option\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

if __name__ == "__main__":
    main()