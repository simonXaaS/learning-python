# In this project I will try to organize my subjects and grades

# Last year subjects and grades below

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# This year subjects and grades below

subjects = ["physics", "calculus", "poetry", "history"] 
grades = [98, 97, 85, 88]

# Creating two-dimensional list combining my subjects and grades

gradebook = [
  ["physics", 98], 
  ["calculus", 97], 
  ["poetry", 85], 
  ["history", 88]
]

# Appending grades for computer science and visual arts to the gradebook list

gradebook.append(["computer science", 6])
gradebook.append(["visual arts", 93])

# Accessing the index of the grade for visual arts class and modifying it to be 5 points greater 

gradebook[5][1] = 97

# Switching from a numerical grade value to a Pass/Fail option for your poetry class

gradebook[2].remove(85) 
gradebook[2].append("Pass")

# Printing the gradebook

print(gradebook)

# Combining this and last year gradebooks 

full_gradebook = last_semester_gradebook +gradebook
print(full_gradebook)