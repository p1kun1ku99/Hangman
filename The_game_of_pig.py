"""
        Project: The Game of Pig
        Author: Isaac Tannenbaum
        Class: The Coder School
        Short description: Roll a dice and add numbers together with addition and lose points and win and totally humiliate the losers.
"""
# Import random for the use of the dice and randomization of names
import random
import time

first_names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Isabella', 'Asgore', 'Dr.', 'John', 'Evan', 'Flowey', 'Harry', 'Ender', 'Steve', 'Toriel', 'Isaac', 'Logan', 'Gourdy', 'Brash', 'Mango', 
               'Wens', 'Sus', 'Vecna', 'Nabstablook', 'Mad Dummy', 'C00lkid', 'Mettaton', 'Bob', 'Mary', 'Annoying Dog', 'Obnoxious Banana', 'Tralalelo Tralala', 'Tung tung', 'The', 'Greater',
               'Lesser', 'Sans', 'Chess', 'Ninja', 'Gaster', 'Mouse pad', 'Python', 'Pig', 'Mr.', 'Mrs.', 'Oof', 'Wrong', 'Bumblebee', 'Window', 'Wind', 'Earth', 'Fire', 'Water', 'Avatar',
               'Angry', 'Jumbo', 'Undyne', 'Monster']

last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Dreemurr', 'Alphys', 'Pork', 'Dranzo', 'Nightmare', 'Potter', 'Dragon', 'Black', 'Loox', 'Toriel', 'Tannenbaum', 
              'Hovarluck', 'Holloway', 'Google', 'Orbi', 'Five', 'Imposter', 'Demagorgon', 'Acid', 'Doe', 'EX', 'Ross', 'Supercalifragilisticexbialidocious', 'Herobrine', 'Dude', 'Duolingo',
              'Los Tralalelos', 'Sahur', 'AAAAAAAAAAAAAAAAA', 'Baugette', 'Pigeon', 'Dog', 'Turtle', 'Master', 'Blaster', 'Brainrot', 'Enemy', 'Element', 'Tortoise', 'Magic', 'Disaster', 
              'Tree', 'Tooth', 'Boot', 'Lava', 'Walk', 'Lose', 'LOL', 'Beast', 'Bird', 'Duck', 'News', 'Josh', 'Engine', 'Toilet', 'Spears', 'knight', 'Kid', 'Lover']

def generate_random_name():
    """Generates a random full name from predefined lists."""
    first = random.choice(first_names)
    last = random.choice(last_names)
    return f"{first} {last}"

def roll_da_dice():
    return random.randint(1,6)

"""

        Character Section - Being Created and Stored

"""
# This class is either going to be a Robot or Human Player
class Enity:
    def __init__(self):
        self.playerType = "robot"
        self.name = ""
        self.turns = 1
        self.turntotal = 0
        self.score = 0

# Where the player information is stored and which current player is being indexed
allPlayers = []
currentPlayer = 0

# Asks the user how many robots or players are participating
playerCount = int(input("How many players are playing? "))
robotsPlaying = str(input("Are robots playing today? (y or n)"))
robotCount = 999999999999999999
if robotsPlaying == 'y':
    while robotCount > playerCount:
        robotCount= int(input("How many robots are playing? "))
if playerCount != 1:
    currentPlayer = 1
    for i in range(playerCount):
        playerT = input(f"Player {str(i + 1)}: Are you a human or robot?")
        allPlayers.append(i + 1)
        allPlayers[i] = Enity()
        if playerT == "human":
            allPlayers[i].playerType = "human"
            allPlayers[i].name = input("What is your name?")    
        else:
            allPlayers[i].name = generate_random_name()
else:
    playerT = input(f"Player {str(1)}: Are you a human or robot?")
    allPlayers.append(1)
    allPlayers[0] = Enity()

"""

        The Main Game Loop

"""
# If you pass or reach 100pts the game ends
while not any(player.score >= 100 for player in allPlayers):
    choice = ""
    if allPlayers[currentPlayer - 1].playerType == "robot":
        if allPlayers[currentPlayer - 1].turntotal == 0:
            choice = 'r'
        elif allPlayers[currentPlayer - 1].turntotal + allPlayers[currentPlayer - 1].score > 100:
            choice = 'b'
        else:
            choice = random.choice(['r', 'b']) 
        time.sleep(1)
    else:
        choice = input("Would you like to roll or bank? ")

    if choice in ("roll", "r"):
        print()
        roll = roll_da_dice()
        if (allPlayers[currentPlayer - 1].playerType == "human"):
            print(f"{allPlayers[currentPlayer - 1].name} rolled a {str(roll)}.")
        else:
            print(f"Player {str(currentPlayer)}, {allPlayers[currentPlayer - 1].name} rolled a {str(roll)}.")
        if roll == 1:
            print(f"You rolled a 1! You get no points for this round!")
            print(f"Now onto the next player")
            allPlayers[currentPlayer - 1].turntotal = 0
            allPlayers[currentPlayer - 1].turns += 1
            print()
            if playerCount == currentPlayer:
                currentPlayer = 1
            elif playerCount != 1:
                currentPlayer += 1
            print()
            print(f"Now onto the next player")
            print(f"Player {str(currentPlayer)}'s turn")
            print(f"Turn {str(allPlayers[currentPlayer - 1].turns)}")
            print(f"Your Current Score is: {str(allPlayers[currentPlayer - 1].score)}")
            print(f"This round you have: {str(allPlayers[currentPlayer - 1].turntotal)}")

        else:
            allPlayers[currentPlayer - 1].turntotal = roll + allPlayers[currentPlayer - 1].turntotal
            print(f"This round you have: {str(allPlayers[currentPlayer - 1].turntotal)}")
    elif choice in ("bank", "b"):
        allPlayers[currentPlayer - 1].turns += 1
        allPlayers[currentPlayer - 1].score += allPlayers[currentPlayer - 1].turntotal
        allPlayers[currentPlayer - 1].turntotal = 0
        print(f"Banking")
        if allPlayers[currentPlayer - 1].score >= 100:
            break
        
        print()
        if playerCount == currentPlayer:
            currentPlayer = 1
        else:
            currentPlayer += 1
        
        print()
        print()
        print(f"Now onto the next player")
        print(f"Player {str(currentPlayer)}'s turn")
        print(f"Turn {str(allPlayers[currentPlayer - 1].turns)}")
        print(f"Your Current Score is: {str(allPlayers[currentPlayer - 1].score)}")
        print(f"This round you have: {str(allPlayers[currentPlayer - 1].turntotal)}")

winner = None
for i, player in enumerate(allPlayers):
    if player.score >= 100:
        winner = i
        break
# Final score and winner
print(f"Congratulations! Player {str(winner + 1)} won in {str(allPlayers[winner].turns)} turns! With a final score of {str(allPlayers[winner].score)   }."
)