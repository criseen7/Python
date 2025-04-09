import re
def RLE_decode(s):
    return ''.join(c * int(n) for c, n in re.findall(r'(\D)(\d+)', s))

def RLE_encode(s):
    result = []
    i=0
    while i<len(s):
        count = 1
        while i+1<len(s) and s[i]==s[i+1]:
            i+=1
            count+=1
        result.append(s[i] + str(count))
        i+=1
    return ''.join(result)

def input_string():
    return input("Enter a phrase: ").strip()

def main():
    while True:
        try:
            opt = int(input("1. Encoder Run-Length Encoding\n2. Decoder Run-Length Encoding\n3.Exit\nChoose an option: "))
            if opt ==1:
                phrase=input_string()
                print(f'Encoder RLE: {RLE_encode(phrase)}')
            elif opt == 2:
                phrase=input_string()
                print(f'Decoder RLE: {RLE_decode(phrase)}')
            elif opt ==3:
                print("Closing...")
                break
            else:
                print("Invalid option. Please enter 1, 2 or 3\n")
        except ValueError:
            print("Invalid input. Plese enter a number\n")

if __name__ == "__main__":
    main()