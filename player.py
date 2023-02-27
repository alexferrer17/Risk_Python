import random

class Player:
    def __init__(self, territories, total_troops):
        self.territories = territories
        self.troops = {territory: troops for territory, troops in zip(territories, total_troops)}

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

    def attack(self, defender, attack_from_territory, attack_to_territory, troops):
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
