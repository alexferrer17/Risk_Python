import random
from player import Player
from territories import Territories

# Create an instance of the Territories class
my_territories = Territories()

# List of all territories in the game
territories = [
    "Alaska", "Northwest Territory", "Greenland",
    "Alberta", "Ontario", "Quebec", "Western United States",
    "Eastern United States", "Central America",
    "Venezuela", "Peru", "Brazil", "Argentina",
    "Iceland", "Great Britain", "Scandinavia", "Northern Europe",
    "Southern Europe", "Ukraine", "Western Europe", "North Africa",
    "Egypt", "East Africa", "Congo", "South Africa",
    "Madagascar", "Ural", "Siberia", "Yakutsk",
    "Kamchatka", "Irkutsk", "Mongolia", "Japan",
    "Afghanistan", "India", "Middle East", "China",
    "Siam", "Indonesia", "New Guinea", "Western Australia",
    "Eastern Australia"
]

# Total number of troops
total_troops = 90

# Total number of player
num_players = 3

# Randomly assign territories to players
random.shuffle(territories)
player1_territories = territories[:14]
player2_territories = territories[14:28]
neutral_territories = territories[28:]

# Distribute troops for player 1
player1_troops = [random.randint(1, 3) for _ in range(14)]

#Ensure that the total troops for player 1 adds to 30
player1_troops = [random.randint(1, total_troops//30) for _ in range(14)]
while sum(player1_troops) != 30:
    index = random.randint(0, 13)
    if sum(player1_troops) < 30:
        player1_troops[index] += 1
    else:
        player1_troops[index] -= 1

# Distribute troops for player 2
player2_troops = [random.randint(1, 3) for _ in range(14)]

#Ensure that the total troops for player 2 adds to 30
player2_troops = [random.randint(1, total_troops//30) for _ in range(14)]
while sum(player2_troops) !=30:
    index = random.randint(0, 13)
    if sum(player2_troops) < 30:
        player2_troops[index] += 1
    else:
        player2_troops[index] -= 1

neutral_troops = [random.randint(1, 3) for _ in range(14)]

# Create Player objects for each player
player1 = Player("player1", player1_territories, player1_troops)
player2 = Player("player2", player2_territories, player2_troops)
neutral = Player("neutral", neutral_territories, neutral_troops)

players = [player1, player2, neutral]

# Print information of each player
for player in players:
    player.print_info()

player1.play_game(players)

"""
# Call the instance method on the instance to test if it works
adj_list = my_territories.read_adjacency_list('territory_data.txt')

if my_territories.is_adjacent('Ukraine', 'Japan', adj_list):
    print('Ukraine is adjacent to Japan')
else:
    print('Ukraine is not adjacent to Japan')
"""
