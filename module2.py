def calculate_future_value(monthly_investment, yearly_interest, years):
    monthly_interest = yearly_interest / 12 / 100

    future_value = 0
    x = 0
    for x in range(0, years):
        x += 1
        for i in range(0, 12):
            future_value += monthly_investment
            monthly_interest_value = future_value * monthly_interest
            future_value += monthly_interest_value
        print(str(x) + str(future_value))
    return
    

monthly_investment = 100
yearly_interest = 12
years = 10

future_value = calculate_future_value(monthly_investment, yearly_interest, years)

print(future_value)
