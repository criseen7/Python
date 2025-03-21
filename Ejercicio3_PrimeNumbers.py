def Prime_Numbers(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
def main():
    while True:
        n = int(input("Enter a number: "))
        print("Es primo" if Prime_Numbers(n)==True else "No es primo")
        option=input("Quieres ingresar otro numero (y/n):")
        if option.lower() != 'y':
            break

if __name__ == "__main__":
    main()