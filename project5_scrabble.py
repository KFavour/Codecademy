letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

## Maps each letter to a point
letter_to_points = {key:value for key,value in zip(letters, points)}
# print(letter_to_points)

letter_to_points[""] = 0
print(letter_to_points)


## Takes word and returns sum of points of each letter
score_word = lambda word:sum([letter_to_points[letter] for letter in word])
# score_word() Test
brownie_points = score_word("BROWNIE")
print(brownie_points)


## Maps each player to a list of words
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}
# print(player_to_words)

## Maps player to sum of points of each of their words
player_to_points = {key:value for key,value in zip(player_to_words.keys(), [sum([score_word(word) for word in words]) for words in player_to_words.values()])}

print(player_to_points)

## Adds a word to list of words player has played
def play_word(player, word):
  player_to_words[player].append(word)
  player_to_points[player]+=score_word(word)
# play_word Test
play_word("player1", "FAVOUR")
play_word("Lexi Con", "FANTASTIC")
play_word("wordNerd", "BRAVE")
print(player_to_words)
print(player_to_points)


