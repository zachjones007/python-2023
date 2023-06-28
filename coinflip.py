import random
winstreak = 0
games = 0
wins = []
h = 'HHHHHH'
t = 'TTTTTT'
counter = t,h
while games < 100: 
    num = random.randint(0, 1)  
    if num == 0:
        wins.append('H')
        print('heads')
        six = "".join(wins[-6:])  # get the last 6 flips
        if six == h or six == t:
            winstreak += 1
            print(winstreak)
    else: 
        wins.append('T')
        print('tails')
        six = "".join(wins[-6:])  # get the last 6 flips
        if six == h or six == t:
            winstreak += 1
            print(winstreak)
    games += 1 
print(f'game over the win streak counter was at :{winstreak}')



            

