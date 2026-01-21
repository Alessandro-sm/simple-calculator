while True:
    try:

        def addition():
            sum = number_a + number_b
            return sum
        
        def subtraction():
            sub = number_a - number_b
            return sub
        
        def multiplication():
            mult = number_a * number_b
            return mult

        def division():
            div = number_a / number_b
            return div

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

            number_a = float(input("Indicate the first number: "))
            number_b = float(input("Indicate the second number: "))

            if choice == 1:
                print(f"The answer is {addition()}")
    
            elif choice == 2:
                print(f"The answer is {subtraction()}")

            elif choice == 3:
                print(f"The answer is {multiplication()}")

            elif choice == 4:
                print(f"The answer is {division()}")

            another = input("Do you want another operation? (yes/no): ").lower()
            if another != "yes" and another != "y":
                break
        
        else:
            print("You can only choose from 0 to 4") 


    except ValueError:
        print("Please enter a valid number")
        break