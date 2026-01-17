while True:
    try:
        print("======== CHOOSE THE OPERATION ========")
        print("1.- Addition")
        print("2.- Subtraction")
        print("0.- Exit")
        choice = int(input("--> "))

        if 0 <= choice <= 2:
            
            if choice == 0:
                break

            number_a = float(input("Indicate the first number: "))
            number_b = float(input("Indicate the second number: "))

            if choice == 1:
                addition = number_a + number_b
                print(f'The answer is {addition}')
    
            elif choice == 2:
                subtraction = number_a - number_b
                print(f'The answer is {subtraction}')
            
            another = input("Do you want another operation? (yes/no): ").lower()
            if another != "yes" and another != "y":
                break
        
        else:
            print("You can only choose from 0 to 2") 


    except ValueError:
        print("Please enter a valid number")   