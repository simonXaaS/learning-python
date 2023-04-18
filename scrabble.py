# In this project, I will process some data from a group of friends playing scrabble. I will use dictionaries to organize players, words, and points.

# I will be starting with two lists, letters and points

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# I will combine these two into a dictionary that would map a letter to its point value

letter_to_points = {
  key:value 
  for key, value 
  in zip(letters, points)
  }

# The letters list did not take into account blank tiles. I will add an element to the letter_to_points dictionary that has a key of " " and a point value of 0

letter_to_points[" "] = 0

print(letter_to_points)

# Now we want to create a function that will take in a word and return how many points that word is worth

def score_word(word):

  point_total = 0

  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  
  return point_total

# Let’s test this function! Create a variable called brownie_points and set it equal to the value returned by the score_word()

brownie_points = score_word("BROWNIE")
print(brownie_points)

#  Create a dictionary called player_to_words that maps players to a list of the words they have played

player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"],
}

# Now I'm creating an empty dictionary called player_to_points

player_to_points = {}

# Iterate through the items in player_to_words. Call each player player and each list of words words

# Within the loop, create another loop that goes through each word in words and adds the value of score_word() with word as an input

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)

# player_to_points should now contain the mapping of players to how many points they’ve scored. Print this out to see the current standings for this game!

  





