# I’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats. In this project, I will be storing the names and prices of a furniture store’s catalog in variables. I will then process the total price and item list of customers, printing them to the output terminal.


# Store shop's first iteam in variable

lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""

# Store price for the item in variable

lovely_loveseat_price = 254.00

# Extend inventory with another item

tylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""

# Set a price for the second item

stylish_settee_price = 180.50

# Create a third item

luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""

# Set price for the 3rd item

luxurious_lamp_price = 52.15

# In order to be a business, we should also be calculating sales tax. Let’s store that in a variable as well

sales_tax = .088

# Purchase section below

customer_one_total = 0

customer_one_itemization = ""

# Our first customer has decided to the lovely seats item

customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

# They also want to buy the luxurious lamp item

customer_one_total += luxurious_lamp_price

customer_one_itemization += luxurious_lamp_description

# We need to add tax to the total price

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

# Printing out receipt

print("Customer One Items:")
print(customer_one_itemization)

print("Total One Total:")
print(customer_one_total)
















