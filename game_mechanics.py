#Game mechanics like attack defend and move troops
def attack(attacker, defender, attacker_dice, defender_dice):
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
            defender['armies'] -= 1
        else:
            attacker['armies'] -= 1
    if defender['armies'] == 0:
        attacker['territories'].append(defender['name'])
        defender['owner'] = attacker['name']



def defend(attacker, defender, attacker_dice, defender_dice):
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
            defender['armies'] -= 1
        else:
            attacker['armies'] -= 1
    if defender['armies'] == 0:
        attacker['territories'].append(defender['name'])
        defender['owner'] = attacker['name']
def move_armies(player, origin, destination, armies):
    if origin in player['territories'] and destination in player['territories']:
        if origin['armies'] >= armies:
            origin['armies'] -= armies
            destination['armies'] += armies
    else:
        print("Invalid move")
