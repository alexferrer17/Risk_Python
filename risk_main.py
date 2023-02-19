import random

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

# Randomly assign territories to players
random.shuffle(territories)
player1_territories = territories[:14]
player2_territories = territories[14:28]
neutral_territories = territories[28:]

# Distribute troops randomly among players
player1_troops = [random.randint(1, total_troops//30) for _ in range(14)]
player2_troops = [random.randint(1, total_troops//30) for _ in range(14)]
neutral_troops = [random.randint(1, total_troops//30) for _ in range(14)]

# Make sure that each player has at most 30 troops
if sum(player1_troops) > 30:
    excess_troops = sum(player1_troops) - 30
    player1_troops[-1] -= excess_troops

if sum(player2_troops) > 30:
    excess_troops = sum(player2_troops) - 30
    player2_troops[-1] -= excess_troops

if sum(neutral_troops) > 30:
    excess_troops = sum(neutral_troops) - 30
    neutral_troops[-1] -= excess_troops

# Dictionary to store information about players
players = {
    "player1": {
        "territories": player1_territories,
        "troops": player1_troops
    },
    "player2": {
        "territories": player2_territories,
        "troops": player2_troops
    },
    "neutral": {
        "territories": neutral_territories,
        "troops": neutral_troops
    }
}

# Print information about players
for player, info in players.items():
    print(f"Player: {player}")
    print(f"Territories: {info['territories']}")
    print(f"Troops: {info['troops']}")
    print("\n")

#Day 1 setup board with all the territories
#Day 2 setup the attacking, defending, and moving troops
