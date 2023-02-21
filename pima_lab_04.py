import random

EXPERIMENTS = 10000
LIST_SIZE = 100
numberOfListsWithStreaks = 0

for experimentNumber in range(EXPERIMENTS):
    # Create a list of LIST_SIZE random 'heads' or 'tails' values.
    flips = [random.choice(['H', 'T']) for i in range(LIST_SIZE)]

    # Check if there is a streak of 6 heads or 6 tails in a row in the list.
    if 'HHHHHH' in ''.join(flips) or 'TTTTTT' in ''.join(flips):
        numberOfListsWithStreaks += 1

print(f'Chance of streak: {(numberOfListsWithStreaks / EXPERIMENTS) * 100:.2f}%')
