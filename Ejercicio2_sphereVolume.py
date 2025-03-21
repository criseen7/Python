import numpy as np
def sphere_volume(radius):
    print(f"The sphere volume is:{4/3*(np.pi*(radius**3)):.2f} cm\n")

def main():
    while True:
        try:
            option = int(input("Choose an option to calculate the sphere volume\n1.Use diameter\n2.Use radius\n3.Use area\n4.Exit\nOption: "))
            if option == 1:
                diameter = float(input("Enter the diameter in cm: "))
                sphere_volume(diameter/2)
            elif option == 2:
                radius = float(input("Enter the radius in cm: "))
                sphere_volume(radius)
            elif option == 3:
                area = float(input("Enter the area in cm: "))
                sphere_volume((area/(4*np.pi))**0.5)
            elif option == 4:
                print("Exiting program...")
                break
            else:
                print("Invalid option. Please choose 1, 2 or 3.\n")
        except ValueError:
            print("Invalid input. Please Enter a number\n")

if __name__ == "__main__":
    main()