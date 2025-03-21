import numpy as np
def Circle_Area(radius):
    print(f"The Circle area is: {np.pi*(radius**2):.2f} cm\n")

def main():
    try:
        while (True):
            option=int(input("1.Use radius\n2.Use diameter\n3.Use circunference\n4.Exit\nChoose an option to calculate the circle area: "))
            if(option == 1):
                radius=float(input("Enter the radius of the circle (in cm): "))
                Circle_Area(radius)
            elif (option == 2):
                diameter=float(input("Enter the diameter of the circle (in cm): ")) 
                Circle_Area(diameter/2)
            elif (option == 3):
                circunference = float(input("Enter the circunference of the circle (in cm): "))
                Circle_Area(circunference/(2*np.pi))
            elif (option == 4):
                print("Exiting program...")
                break
            else:
                print("Invalid option. Please enter 1, 2 or 3.\n")
    except ValueError:
        print("Invalid input. Please enter a number")


if __name__ == "__main__":
    main()