#https://retosdeprogramacion.com/ejercicios/

#1 El Famoso "FIZZ BUZZ"
'''
* Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
* - Múltiplos de 3 por la palabra "fizz".
* - Múltiplos de 5 por la palabra "buzz".
* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''
def FizzBuzz():
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0: 
            print("fizzbuzz")
        elif i%3 == 0: 
            print("fizz")
        elif i%5 == 0: 
            print("buzz")
        else:
            print(i)
    return 0

#2 ¿Es un anagrama?
'''
* Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODASlas letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
'''
def anagrama(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if str1 == str2:
        return False
    return sorted(str1) == sorted(str2)

#3 La Sucesion de Fibonacci
'''
* Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
'''
def Fibonacci():
    a=[0,1]
    for i in range(2,51):
        a.append(a[i-2] + a[i-1])
    print(a)

#4 ¿Es un numero primo?
'''Escribe un programa que se encargue de comprobar si un número es o no primo. Hecho esto, imprime los números primos entre 1 y 100.'''
def EsPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def primos():
    nPrimos = []
    for i in range(1,101):
        if EsPrimo(i):
            nPrimos.append(i)
    print(f"Los numeros primos entre 1 y 100 son:\n{nPrimos}")

def main():
    try:
        while True:
            opt = int(input("**********Menu**********\n1.-FizzBuzz\n2.-¿Es Anagrama?\n3.-Fibonacci\n4.-¿Es número primo?\nElige una opción:"))
            match opt:
                case 1:
                    FizzBuzz()
                case 2:
                    while True:
                        p1 = input("Ingresa una palabra: ")
                        p2 = input("Ingresa otra palabra: ")
                        print(anagrama(p1,p2))
                        y = input("Quieres ingresar más palabras (y/n): ").lower().strip()
                        if y!="y":
                            break
                case 3:
                    Fibonacci()
                case 4:
                    n = int(input("Ingresa un número: "))
                    if EsPrimo(n):
                        print(f"El numero '{n}' es un numero primo")
                    else:
                        print(f"El numero '{n}' no es un numero primo")
                    primos()
                case _:
                    print("\nSaliendo...")
                    break
    except ValueError:
        print("Invalid input. Please enter a number")
                    

if __name__ == "__main__":
    main()