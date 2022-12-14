def calculate_future_value(monthly_investment, yearly_interest_rate, years):
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    future_value = 0.0
    x = 0
    for x in range(0, years):
        x += 1
        for i in range(0, 12):
            future_value += monthly_investment
            monthly_interest = future_value * monthly_interest_rate
            future_value += monthly_interest
        print("Years: " + str(x) + " Future Value = " + str(round(future_value, 2)))
    return

def main():
    choice = "y"
    while choice.lower() == "y":

        while True:
            monthly_investment = float(input("Enter monthly investment:\t"))
            if monthly_investment <= 0:
                print("Entry must be greater than 0. Please try again.")
            else:
                break

        while True:
            yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
            if yearly_interest_rate <= 0 or yearly_interest_rate > 15:
                print("Entry must be greater than 0 and less than or equal to 15.\nPlease try again.")
            else:
                break

        while True:
            years = int(input("Enter number of years:\t\t"))
            if years <=0 or years > 50:
                print("Entry must be greater than 0 and less than or equal to 50.\nPlease try again")
            else:
                break
        
        future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years)
        print(future_value)

        choice = input("Continue? (y/n): ")

        while True:
            if choice.lower() == "y":
                break
            elif choice.lower() == "n":
                break
            else:
                choice = input("Error, Continue? (y/n): ")
        

    print("Bye!")

if __name__ == "__main__":
    main()