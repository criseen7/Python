def invertString(text):
    return text[::-1]

def main():
    while True:
        text = input("Enter a string: ")
        print(f"The invert string is: {invertString(text)}\n")
        option=input("Do you want enter another string?(y/n) ")
        if option.lower() != "y":
            break

if __name__ == "__main__":
    main()