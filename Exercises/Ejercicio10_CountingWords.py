from collections import Counter
def counting_words(s):
    return Counter(s)

def main():
    while True:
        phrase = input("Enter a phrase: ").lower().split()
        print(f'Counting Words:\n{counting_words(phrase)} \n')
        opt = input("Do you want enter another phrase?(y/n) ").lower().strip()
        if opt != 'y':
            break

if __name__ == '__main__':
    main()