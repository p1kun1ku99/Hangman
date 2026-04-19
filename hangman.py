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
      monkey moose mouse mule newt otter owl panda parrot pidgeon python rabbit \
      ram rat raven rhino salmon seal shark sheep skunk sloth snake \
      spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

# for frame in HANGMAN_PICS:
#   print(frame)

for word in words:
  print(word)
