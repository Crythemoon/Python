import module_test as mt

def display():
    print("Welcome to the Future Value Calculator\n")

def main():
    display()
    choice = "y"
    while choice.lower() == "y":
        mi = int(input("Enter monthly investment:\t\t"))
        while mi <= 0 and mi > 1000:
            print("Entry must be greater than 0 and lesss than or equal to 1000")
            mi = int(input("Enter monthly investment:\t\t"))

        yi = int(input("Enter yearly interest rate:\t\t"))
        while yi <= 0 and yi > 15:
            print("Entry must be greater than 0 and less than or equal to 15")
            yi = int(input("Enter yearly interest rate:\t\t"))

        y = int(input("Enter number of years:\t\t"))
        while y <= 0 and y > 50:
            print("Entry must be greater than 0 and less than 50")
            y = int(input("Enter number of years:\t\t"))

        choice = input("Continue (y/n)? ")
        while True:
            if choice.lower() == "y":
                break
            elif choice.lower() == "n":
                break
            else:
                print("Please choose a valid response")
                choice = input("Continue (y/n)? ")
        fv = mt.calculator(mi, yi, y)
        print(fv)

    print("Good Bye")

if __name__ == "__main__":
    main()