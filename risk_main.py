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
player1 = Player(player1_territories, player1_troops)
player2 = Player(player2_territories, player2_troops)
neutral = Player(neutral_territories, neutral_troops)

# Dictionary to store information about players
players = {
    "player1": player1,
    "player2": player2,
    "neutral": neutral
}

# Print information about players
for player, obj in players.items():
    print(f"Player: {player}")
    for territory in obj.territories:
        troop_count = obj.troops[territory]
        print(f"{territory}: {troop_count} troops")
    print()

# Call the instance method on the instance to test if it works
adj_list = my_territories.read_adjacency_list('territory_data.txt')

if my_territories.is_adjacent('Ukraine', 'Japan', adj_list):
    print('Ukraine is adjacent to Japan')
else:
    print('Ukraine is not adjacent to Japan')

#Ask user to input and see if the territories work

# Ask the user to input two territories
territory1 = input("Enter the name of the first territory: ")
territory2 = input("Enter the name of the second territory: ")

# Check if the user input is valid
if territory1 in player1.territories and territory2 in player1.territories and territory1 != territory2:
    # The user input is valid
    print(f"You have selected to move troops from {territory1} to {territory2}")
else:
    # The user input is not valid
    print("Invalid input. Please enter two different territories that are owned by the first player.")

# Get the input from the user
from_territory = input("Enter the name of the territory from which you want to move troops: ")
to_territory = input("Enter the name of the territory to which you want to move troops: ")
num_troops = int(input("how many troops do you want to move: "))

#checks if there are enough troops
if(num_troops >= player1.troops[from_territory]):
    print("You can't move that amount of troops")
else:
    # Update the number of troops for the from_territory and to_territory
    player1.troops[from_territory] -= num_troops
    player1.troops[to_territory] += num_troops
    print("The move has been successful, here are the new amount of troops from " + to_territory + ": " + str(player1.troops[to_territory]))
