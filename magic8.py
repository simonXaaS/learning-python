# The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking. Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

# Importing random module

import random

# Declaring variables below

name = "Simon"
question = "am I a good DevOps Engineer?"
answer = ""

# Declaring random.randit function in variable to generate random numbers from range

import random

random_number = random.randint(1, 9)
print(random_number)

# Now that we’ve declared all the variables needed, it’s time to implement the core logic of our program

if random_number == 1: 
  answer = " Yes - definitely"
elif random_number == 2: 
  answer = " It is decidedly so"
elif random_number == 3: 
  answer = " Without a doubt"
elif random_number == 4: 
  answer = " Reply hazy, try again"
elif random_number == 5: 
  answer = " Ask again later"
elif random_number == 6: 
  answer = " Better not tell you now"
elif random_number == 7: 
  answer = " My sources say no"
elif random_number == 8: 
  answer = " Outlook not so good"
elif random_number == 9: 
  answer = " Very doubtful"
else:
  answer = " Error"

# Adding print statements that will output the asker’s name / question and Magic 8-Ball’s answer

print(name + " asks: " + question)
print("Magic 8-Ball's answer:" + answer)
