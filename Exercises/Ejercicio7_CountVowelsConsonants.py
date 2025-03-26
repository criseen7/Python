def count_vowels_consonants(S):
    vowels = 'aeiouAEIOU'
    v = sum(1 for c in S if c in vowels)
    c = sum(1 for c in S if c.isalpha() and c not in vowels)
    return v, c

def main():
    while True:
        text = input('Enter a string: ').strip()  # Eliminamos espacios innecesarios
        print(f'Vowels: {count_vowels_consonants(text)[0]}, Consonants: {count_vowels_consonants(text)[1]}')
        option = input('Do you want to enter another string? (y/n) ').strip().lower()
        if option != 'y':
            print("Exiting...")
            break

if __name__ == '__main__':
    main()
