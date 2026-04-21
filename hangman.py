"""
        Project: Hangman
        Author: Isaac Tannenbaum
        Class: The Coder School
        Short description: There's a word. But you don't know the word. So you can guess letters to fill in the blank. But you only have 5 tries.
"""
# Import random for the use of the dice and randomization of names
import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
    ====''','''
  +---+
  O   |
      |
      |
    ====''','''
  +---+
  O   |
  |   |
      |
    ====''','''
  +---+
  O   |
/ |   |
      |
    ====''','''
  +---+
  O   |
/ | \ |
      |
    ====''','''
  +---+
  O   |
/ | \ |
 /    |
    ====''','''
  +---+
  O   |
/ | \ |
 / \  |
    ====''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra \
      cougar coyote crow deer dog donkey duck eagle elk ferret \
      fox frog goat goose gorrilla hawk lion lizard llama mole  \
      monkey moose mouse mule newt otter owl panda parrot pidgeon python \
      rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake \
      spider stork swan tiger toad trout turkey turtle weasel whale wolf \
      wombat zebra chair oven couch television cabinet computer desk mousepad \
      trash bin basket button door light paint book safety determination \
      supernatural compound communication vespa spaghetti meat lettuce pizza \
      taco ice cream cake candle cookie bacon egg hot dog cat hamburger \
      lettuce cheese cheesecake darkness number game video dollar percentage \
      bulb seed arrow bow man woman fish invent potion checkers chess fire \
      water elf wind air month year day week hour minute second first third \
      fourth star sun moon glass glasses place person thing banana apple'.split()

# for frame in HANGMAN_PICS:
#   print(frame)

# for word in words:
#   print(word)

def get_random_word(words_list):
  word_index = random.randint(0, len(words_list) -1)
  return words_list[word_index]

print(get_random_word(words))

def display_the_board(missed_letters, correct_letters, secret_word):
  print(HANGMAN_PICS[len(missed_letters)])
  print()

  print('Missed letters:', end=' ')
  for letter in missed_letters:
    print(letter, end=' ')
  print()

  blanks = ' ' * len(secret_word)

  for i in range(len(secret_word)):
    if secret_word[i] in correct_letters:
      blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

  for letter in blanks:
    print (letter, end=' ')
  print()













missed_letters = ''
correct_letters = ''

display_the_board()
