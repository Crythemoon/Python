future_value = 0
monthly_investment = 100
monthly_interest = 12 / 1200

for i in range(12):
            future_value += monthly_investment
            monthly_interest_amount = future_value * monthly_interest
            future_value += monthly_interest_amount
            print(str(future_value) + " " + str(i))