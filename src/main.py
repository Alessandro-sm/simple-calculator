from operations import addition, subtraction, multiplication, division

while True:
    try:
        print("======== CHOOSE THE OPERATION ========")
        print("=> 1.- Addition")
        print("=> 2.- Subtraction")
        print("=> 3.- Multiplication")
        print("=> 4.- Division")
        print("=> 0.- Exit")
        
        choice = int(input("--> "))

        if 0 <= choice <= 4:
            if choice == 0:
                break

            a = float(input("Indicate the first number: "))
            b = float(input("Indicate the second number: "))

            if choice == 1:
                print(f"The answer is {addition(a, b)}")
    
            elif choice == 2:
                print(f"The answer is {subtraction(a, b)}")

            elif choice == 3:
                print(f"The answer is {multiplication(a, b)}")

            elif choice == 4:
                result = division(a, b)
                if result == "Error":
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"The answer is {result}")

            another = input("Do you want another operation? (yes/no): ").lower()
            if another != "yes" and another != "y":
                break
        
        else:
            print("You can only choose from 0 to 4") 


    except ValueError:
        print("Please enter a valid number")
        break