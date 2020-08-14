
def menu():
    print("Here is the menu: ")
    print("1. Soup and salad")
    print("2. Pasta with meat sauce")
    print("3. Chef's special")

    num = int(input("Which number would you like to order? "))

    #make a while loop
    #while num is not in range, ask again for user input.
    while(num != 1 and num != 2 and num != 3):
        num = int(input("Please choose a valid number (1,2,3)"))

    if(num == 1):
        print("One soup and salad coming right up! ")
    elif(num == 2):
        print("One pasta with meat sauce coming right up!")
    elif(num == 3):
        print("One chef's special coming right up!")


menu()