import random

class Player:
    def __init__(self, territories, total_troops):
        self.territories = territories
        self.troops = {territory: troops for territory, troops in zip(territories, total_troops)}

    def attack(self, defender, attacker_dice, defender_dice):
        attacker_rolls = []
        defender_rolls = []
        for i in range(attacker_dice):
            attacker_rolls.append(random.randint(1, 6))
        for i in range(defender_dice):
            defender_rolls.append(random.randint(1, 6))
        attacker_rolls.sort(reverse=True)
        defender_rolls.sort(reverse=True)
        for i in range(min(len(attacker_rolls), len(defender_rolls))):
            if attacker_rolls[i] > defender_rolls[i]:
                defender.troops -= 1
            else:
                self.troops -= 1
        if defender.troops == 0:
            self.territories.append(defender)
            defender.owner = self

    def defend(self, attacker, attacker_dice, defender_dice):
        attacker_rolls = []
        defender_rolls = []
        for i in range(attacker_dice):
            attacker_rolls.append(random.randint(1, 6))
        for i in range(defender_dice):
            defender_rolls.append(random.randint(1, 6))
        attacker_rolls.sort(reverse=True)
        defender_rolls.sort(reverse=True)
        for i in range(min(len(attacker_rolls), len(defender_rolls))):
            if attacker_rolls[i] > defender_rolls[i]:
                self.troops -= 1
            else:
                attacker.troops -= 1
        if self.troops == 0:
            attacker.territories.append(self)
            self.owner = attacker

    def move_armies(self, origin, destination, armies):
        if origin in self.territories and destination in self.territories:
            if origin.troops >= armies:
                origin.troops -= armies
                destination.troops += armies
            else:
                print("Not enough armies in origin territory.")
        else:
            print("Invalid move.")
