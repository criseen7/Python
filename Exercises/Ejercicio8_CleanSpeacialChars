import re #expresiones regulares
def Clean_string(S):
    return re.sub(r'[^A-Za-z0-9]','',S)#Todo lo que no este de  la "A" a la "Z", "a"-"z o del "0"-"1", vacialo. del string

def main():
    while True:
        text = input("Enter a string: ")
        print(Clean_string(text))
        option = input("Do you want enter another string(y/n)? ").strip().lower()
        if option != 'y':
            break

if __name__ == "__main__":
    main()
