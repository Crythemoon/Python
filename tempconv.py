import temp

def display_menu():
    print("MENU")
    print("1. Fahrenheit to Celcius")
    print("2. Celsius to Fahrenhit\n")

def convert_temp():
    while True:
        option = int(input("Enter a menu option: "))

        if option == 1:
            f = int(input("Enter degrees Fahrenheit: "))
            c = temp.to_celsius(f)
            print("Degrees Celsius: " + str(round(c, 2)))
            break

        elif option == 2:
            c = int(input("Enter degrees Celsius: "))
            f = temp.to_fahrenheit(c)
            print("Degrees Fahrenheit: " + str(round(f, 2)))
            break

        else:
            print("You must enter a valid menu number.")

def main():
    display_menu()
    choice = "y"
    while choice.lower() == "y":
        convert_temp()
        print()
        choice = input("Convert another temperature? (y/n): ")
        
        while True:
            if choice.lower() == "y":
                break
            elif choice.lower() == "n":
                break
            else:
                choice = input("Please enter a valid response (y/n): ")
        print()

    print("Good Bye!")

if __name__ == "__main__":
    main()