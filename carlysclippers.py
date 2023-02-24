# I'm the the Data Analyst at Carly’s Clippers shop. My job is to go through the lists of data that have been collected in the past couple of weeks. 

# I will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

# I have been provided with below three lists. Each index in hairstyles corresponds to an associated index in prices and last_week.

# The names of the cuts offered at Carly’s Clippers

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# The price of each hairstyle in the hairstyles list

prices = [30, 25, 40, 20, 20, 35, 50, 35]

# The number of purchases for each hairstyle type in the last week

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# First I need to find out what average price of a cut is

total_price = 0 
for price in prices:
  total_price += price  
average_price = total_price / len(prices)
print("Average Price: ${0}".format(average_price))

# The average price is more expensive than Carly thought it would be. I will use list comprehension to make a list called new_prices, which has each element in prices minus 5

new_prices = [price - 5 for price in prices]
print(new_prices)

# Carly wants to know how much revenue was brought in last week

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: ${0}".format(total_revenue))

#  Calculating daily revenue of last week

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: ${0}".format(total_revenue))

# Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)





