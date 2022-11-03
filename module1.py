print("Welcome to the Future Value Calculator")

answer = "y"

while answer.lower() == "y":
    print()

    while True:
        monthly_investment = int(input("Enter monthly investment:\t"))
        if monthly_investment <= 0:
            print("Entry must be greater than 0. Please try again.")
        else:
            break
   
    while True:
        yearly_interest = int(input("Enter yearly interest rate:\t"))
        if yearly_interest <= 0 or yearly_interest > 15:
            print("Entry must be greater than 0 and less than or equal to 15\nPlease try again.")
        else:
            break
    monthly_interest = float(yearly_interest / 1200)

    while True:
        number_years = int(input("Enter number of years:\t\t"))
        if number_years <=0 or number_years > 50:
            print("Entry must be greater than 0 and less than or equal to 50.\nPlease try again")
        else:
            break
    
    print()

    future_value = 0
    year = 0
    while year < number_years:
        for i in range(12):
            future_value += monthly_investment
            monthly_interest_amount = future_value * monthly_interest
            future_value += monthly_interest_amount
        year += 1
        print("Year =\t" + str(year) + "\tFuture Value =\t" + str(round(future_value, 2)))

    answer = input("\nContinue (y/n)? ")
    while True:
        if answer.lower() == "y":
            break
        elif answer.lower() == "n":
            break
        else:
            answer = input("Error, try again (y/n)? ")

print("Good Bye!")