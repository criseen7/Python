def calculeFibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci  # Return the entire Fibonacci list

def printFibonacci(fibonacci):
    # Print the Fibonacci sequence on one line, with each number separated by a space
    print(" ".join(map(str, fibonacci)))

def main():
    while True:
        try:
            n = int(input("Enter the number of Fibonacci numbers to calculate: "))
            fibonacci_sequence = calculeFibonacci(n)  # Get the full Fibonacci sequence
            printFibonacci(fibonacci_sequence)  # Print the Fibonacci sequence
            option=input("Quieres ingresar otro numero (y/n):")
            if option.lower() != 'y':
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
