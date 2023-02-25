# I have used my knowledge of Python functions to build out TripPlanner v1.0

# First we want to make sure to welcome our users to the application

def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("Simon")

# Next, we are going to define a function called estimated_time_rounded() that will allow us to calculate a rounded time value based on a decimal for our user’s trip

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(3.5)

# Lastly, we are going to write four print() statements in another function called destination_setup. The estimated_time paramenter will take advanted of the estimated_time_rounded function we created earlier

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("London", "Manchester", estimate)
