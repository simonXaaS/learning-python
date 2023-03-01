# Sal runs the biggest shipping company in the Manchester area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages

# In this project, I'll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers

# We have three different types of shipping: Ground, Premium and Drone

# Ground shipping
# 2 lb or less	$1.50 +	$20.00
# Over 2 lb but less than or equal to 6 lb	$3.00	+ $20.00
# Over 6 lb but less than or equal to 10 lb	$4.00	+ $20.00
# Over 10 lb	$4.75	+ $20.00

def shipping_cost_ground(weight):

    if weight <= 2:
      cost = 1.50
    elif weight <= 6:
      cost = 3.00 
    elif weight <= 10:
      cost = 4.00 
    else:
      cost = 4.75 
    
    return 20 + (cost * weight)

print(shipping_cost_ground(8.4))

# Premium Ground Shipping

shipping_cost_premium = 125.00
print(shipping_cost_premium)

# Drone Shipping
# 2 lb or less	$4.50	$0.00
# Over 2 lb but less than or equal to 6 lb	$9.00	
# Over 6 lb but less than or equal to 10 lb	$12.00
# Over 10 lb	$14.25

def shipping_cost_drone(weight):

  if weight <= 2:
    cost = 4.50 
  elif weight <= 6:
    cost = 9.00 
  elif weight <= 10:
    cost = 12.00 
  else:
    cost = 14.25 

  return cost * weight

print(shipping_cost_drone(2))

# Lastly we create our final function that will call the first two fucntions and use it to calculate the cheapest shipping option

def print_cheapest_shipping_method(weight):
  
  ground = shipping_cost_ground(weight)
  premium = shipping_cost_premium
  drone = shipping_cost_drone(weight)

  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else: 
    method = "drone"
    cost = drone

  print(
    "The cheapest option available is £%.2f with %s shipping." 
    % (cost, method)  
  )

print_cheapest_shipping_method(4.8)


