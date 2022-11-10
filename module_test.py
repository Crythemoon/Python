def calculator(years, monthly_investment, yearly_interest):
    future_value = 0
    x = 1
    while x < years:
        while i in range(12):
            future_value += monthly_investment
            monthly_interest = future_value * float(yearly_interest / 12 / 1000)
            future_value += monthly_interest
            fv = "Future_Value\t\t\t\t:" + str(future_value) + "\n"
        x += 1
    return fv