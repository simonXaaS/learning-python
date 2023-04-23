# The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. My mission is threefold. I must acquire access to The Fender‘s systems, I must update his "passwords.txt" file to scramble the secret data. The last thing I need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat

# I will use my knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for justice. I will work with CSV files and other text files in this exploration of the strength of Python file programming

# I've opened up a communications link to The Fender‘s secret computer. I need you to write a program that will read in the compromised usernames and passwords that are stored in a file called "passwords.csv"

# First I will import the CSV module

import csv
import json

# We need to create a list of users whose passwords have been compromised, create a new list and save it to the variable compromised_users

compromised_users = []

#  Next I’ll need to open up the file itself. Store it in a file object called password_file. Then pass the password_file object holder to our CSV reader for parsing. Save the parsed csv.DictReader object as password_csv

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)

# Create a for loop and save each row of the CSV into the temporary variable password_row
# Inside your for loop, print out password_row['Username']. This is the username of the person whose password was compromised

  for password_row in password_csv:
    #print(password_row['Username'])

# Use the list’s .append() method to add the username to compromised_users instead of printing them

    compromised_users.append(password_row['Username'])

# Start a new with block, opening a file called compromised_users.txt. Open this file in write-mode, saving the file object as compromised_user_file

with open('compromised_users.txt', 'w') as compromised_user_file:

# Inside the new context-managed block opened by the with statement start a new for loop and iterate over each of your compromised_users
# Write the username of each compromised_user in compromised_users to compromised_user_file

  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user + '\n')

# Next, my boss needs to know that I was successful in retrieving the compromised data. I'll need to send him an encoded message over the internet. Let’s use JSON to do that..

# Start by importing JSON at the top of this script

# Open a new JSON file in write-mode called boss_message.json. Save the file object to the variable boss_message

with open('boss_message.json', 'w') as boss_message:

# Create a Python dictionary object within your with statement that relays a boss message. Call this boss_message_dict

  boss_message_dict = {
    "recipient": "The Boss", 
    "message": "Mission Success"
    }

  json.dump(boss_message_dict, boss_message)

# Now that I’ve safely recovered the compromised users I’ll want to remove the "passwords.csv" file completely

# Create a new with block and open "new_passwords.csv" in write-mode. Save the file object to a variable called new_passwords_obj

with open('new_passwords.csv', 'w') as new_passwords_obj:

# Enemy of the people, Slash Null, is who we want The Fender to think was behind this attack. He has a signature, whenever he hacks someone he adds this signature to one of the files he touches

# Write slash_null_sig to new_passwords_obj. Now we have the file to replace passwords.csv with!

  slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)





