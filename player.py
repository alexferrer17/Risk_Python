import random

class Player:
    def __init__(self, name, territories, total_troops):
        self.name = name
        self.territories = territories
        self.troops = {territory: troops for territory, troops in zip(territories, total_troops)}

    def print_info(self):
        print(f"Player: {self.name}")
        print("Territories:")
        for territory in self.territories:
            print(f"  - {territory} ({self.troops[territory]} troops)")

    def move_troops(self, from_territory, to_territory, num_troops):
        """
        Move `num_troops` troops from `from_territory` to `to_territory`.
        """
        if num_troops >= self.troops[from_territory]:
            print("You can't move that amount of troops.")
        else:
            # Update the number of troops for the from_territory and to_territory
            self.troops[from_territory] -= num_troops
            self.troops[to_territory] += num_troops
            print("The move has been successful, here are the new amount of troops from " + to_territory + ": " + str(self.troops[to_territory]))

    def attack(self, defender, attack_from_territory, attack_to_territory):
        attacking_troops = self.troops[attack_from_territory]
        defending_troops = defender.troops[attack_to_territory]

        # roll dice for attacker
        attack_dice = []
        for i in range(attacking_troops):
            attack_dice.append(random.randint(1, 6))
        attack_dice.sort(reverse=True)

        # roll dice for defender
        defense_dice = []
        for i in range(defending_troops):
            defense_dice.append(random.randint(1, 6))
        defense_dice.sort(reverse=True)

        # compare dice rolls
        for i in range(min(attacking_troops, defending_troops)):
            if attack_dice[i] > defense_dice[i]:
                defender.troops[attack_to_territory] -= 1
                print(f"Defender won the attack play with {defense_dice[i]} vs {attack_dice[i]}")
            else:
                self.troops[attack_from_territory] -= 1
                print(f"Attacker won the attack play with {attack_dice[i]} vs {defense_dice[i]}")

        # check if the attack was successful
        if defender.troops[attack_to_territory] == 0:
            defender.remove_territory(attack_to_territory)
            self.add_territory(attack_to_territory)
        elif attacking_troops == 1:
            self.troops[attack_from_territory] -= 1

    def add_territory(self, territory):
        self.troops[territory] = 1

    def remove_territory(self, territory):
        del self.troops[territory]

    def add_troops(self):
        # Check if the player has at least 12 territories
        if len(self.territories) < 12:
            print("You need at least 12 territories to add extra troops.")
            return

        # Calculate the number of extra troops the player gets based on the number of territories they have
        num_extra_troops = max((len(self.territories) // 3) - 3, 0) + 3

        # Prompt the player to add troops to their territories
        print(f"You have {num_extra_troops} extra troops to add.")
        for territory in self.territories:
            while True:
                try:
                    num_troops = int(input(f"How many troops do you want to add to {territory}? "))
                    if num_troops > num_extra_troops:
                        print("You don't have enough extra troops for that.")
                        continue
                    else:
                        self.troops[territory] += num_troops
                        num_extra_troops -= num_troops
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")

                if num_extra_troops == 0:
                    print("You have no more extra troops to add.")
                    return



    def play_game(self, players):
        num_players = len(players)
        current_player = 0

        # Game loop
        while True:
            print(f"\n{players[current_player].name}'s turn:")
            # Stage 1: Add troops
            players[current_player].add_troops()

            # Stage 2: Attack
            print("Which player do you want to attack?")
            for i, player in enumerate(players):
                print(f"{i+1}. {player.name}")
            while True:
                try:
                    player_choice = int(input("Enter the number of the player you want to attack: "))
                    if player_choice < 1 or player_choice > len(players):
                        print("Invalid player choice.")
                        continue
                    else:
                        defender = players[player_choice-1]
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Prompt the user to slect a territory to attack from
            attack_from_territory = None
            print(f"You are attacking {defender.name}.")
            print("Which territory do you want to attack? from")
            for i, territory in enumerate(players[current_player].territories):
                print(f"{i+1}. {territory}")
            while True:
                try:
                    territory_choice = int(input("Enter the number of the territory you want to attack: "))
                    if territory_choice < 1 or territory_choice > len(players[current_player].territories):
                        print("Invalid territory choice.")
                        continue
                    else:
                        attack_from_territory = players[current_player].territories[territory_choice-1]
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Prompt the user to select a territory to attack
            print(f"You are attacking {defender.name}. from {attack_from_territory}")
            print("Which territory do you want to attack?")
            for i, territory in enumerate(defender.territories):
                print(f"{i+1}. {territory}")
            while True:
                try:
                    territory_choice = int(input("Enter the number of the territory you want to attack: "))
                    if territory_choice < 1 or territory_choice > len(defender.territories):
                        print("Invalid territory choice.")
                        continue
                    else:
                        attack_to_territory = defender.territories[territory_choice-1]
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Check if the player already owns the territory
            if attack_to_territory in players[current_player].territories:
                print("You already own that territory.")
                continue

            # Prompt the user to set the amount of troops he wants to use to attack
            players[current_player].print_info()
            troops = input(print("How many troops do you want to use: "))

            # Call the attack method
            players[current_player].attack(defender, attack_from_territory, attack_to_territory)

            # Stage 3: Move troops
            while True:
                from_territory = input("Enter the name of the territory you want to move troops from (or type 'end' to end the turn): ")
                if from_territory == "end":
                    break
                elif from_territory not in players[current_player].territories:
                    print("You don't own that territory.")
                    continue

                to_territory = input("Enter the name of the territory you want to move troops to: ")
                if to_territory not in players[current_player].territories:
                    print("You don't own that territory.")
                    continue
                elif to_territory == from_territory:
                    print("You can't move troops to the same territory.")
                    continue

                num_troops = int(input("Enter the number of troops to move: "))
                players[current_player].move_troops(from_territory, to_territory, num_troops)

            # Check if the current player has won
            if len(players[current_player].territories) == "":
                print(f"{players[current_player].name} has won the game!")
                break

            # Move to the next player's turn
            current_player = (current_player + 1) % num_players
