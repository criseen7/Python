def is_palindrome(s):
    s=''.join(c.lower() for c in s if c.isalnum())#elimina los espacios y caracteres especiales
    return s == s[::-1]

def main():
    while True:
        frase = input("Enter a phrase: ")
        print('The phrase is palindrome' if is_palindrome(frase) == True else "The phrase isn't palindrome")#if ternario
        option = input("Do you want enter another phrase(y/n)? ").strip().lower()
        if option != 'y':
            break

if __name__ == "__main__":
    main()
