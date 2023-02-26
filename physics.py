# You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions that will help them calculate some fundamental physical properties.

# I have defined a few variables we will use later in the script

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# I will start by writing a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# to test the function define a variable f100_in_celsius and set it equal to the value of f_to_c with 100 as an input

f100_in_celsius = f_to_c(100)

# I will write another function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit

def c_to_f(c_temp):
  f_temp = (c_temp * 9/5) + 32
  return f_temp

# Again to test it I'm defining a variable c0_in_fahrenheit and setting it equal to the value of c_to_f with 0 as an input

c0_in_fahrenheit = c_to_f(0)

# Define a function called get_force that takes in mass and acceleration. It should return mass multiplied by acceleration

def get_force(mass, acceleration):
  return mass * acceleration

# Test get_force by calling it with the variables train_mass and train_acceleration at the top of the script

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Next define a function called get_energy that takes in mass and c
# c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8
# get_energy should return mass multiplied by c squared

def get_energy(mass, c=3*10**8):
  return mass * c**2

# I will test get_energy by using it on bomb_mass, with the default value of c and save the result to a variable called bomb_energy

bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# Define a final function called get_work that takes in mass, acceleration, and distance

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

# Test get_work by using it on train_mass, train_acceleration, and train_distance. Save the result to a variable called train_work

print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")

