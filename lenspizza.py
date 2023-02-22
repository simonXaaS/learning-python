# I work at Len’s Slice, a new pizza place in the neighborhood. I'm going to use my knowledge of Python lists to organize some of our sales data.

# Creating a list of pizzas

toppings = [
"pepperoni",
"pineapple",
"cheese",
"sausage",
"olives",
"anchovies",
"mushrooms"
]

# Creating a list of prices

prices = [2, 6, 1, 3, 2, 7, 2]

# Counting the number of occurrences of 2 in the prices list, and storing the result in a variable

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Printing the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas

num_pizzas = len(toppings)
print("We sell {} different kinds of pizza!".format(num_pizzas))
# I could also do this using f-strings. The code would look like this > print(f"We sell {num_pizzas} different kinds of pizza!")

# Creating a new two-dimensional list called pizza_and_prices

pizza_and_prices = list(zip(prices, toppings))
print(pizza_and_prices)

# Sorting the pizzas so they are in the order of increasing price (ascending) and storing the chapest pizza in variable 

cheapest_pizza = pizza_and_prices.sort()
print(pizza_and_prices)

# Getting the last / most expensive pizza from the list and storing it in variable

priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# Removing the most expensive pizza from the list

pizza_and_prices.pop()
print(pizza_and_prices)

# Adding new pizza topping [2.5, "peppers"] to replace "anchovies"
# to position it relative to the rest of the sorted data

pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# Slicing the pizza_and_prices list and storing the 3 lowest cost pizzas in a list called three_cheapest

three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)




