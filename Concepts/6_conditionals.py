#CONDITIONAL STATEMENTS
list = []

list.append("Salsa")

if list:
    print("The list is not empty.") 
else:
    print ("The list is empty.")

# relational operators:  < > <= >= == !=
#logical operators: and or
age = 17
if age < 13:
    print("You are a child.")
elif age >= 13 and age <=17:
    print("you are a teenager")
else:
    print("You are an adult.")
