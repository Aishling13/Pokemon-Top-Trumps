from randomPokemon import random_pokemon
from getPokemon import get_pokemon
from combinePokemonImage import show_combined_pokemon
import time

# Introduction
print(' _________________________________________________________ ')
print('|                                                         |')
print('|                                                         |')
print('| Hello! Welcome to the Pokemon Top Trumps Battle Ground! |')
print('|                                                         |')
print('|                                                         |')
print(' ---------------------------------------------------------')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
trainer_name = input("What is your Super Cool Pokemon trainer name? ")

# Set point limit
limit = int(input("At how many points would you like to end the game?: "))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("Randomly select a pokemon and compare stats. Whoever gets to {} points first wins!".format(limit))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Setting scores
my_score = 0
opponent_score = 0

# Start of Loop
while my_score or opponent_score < limit:

    # Choosing pokemon and showing stats
    print(f'Choose a Pokemon, {trainer_name}!')
    pokemon_name = input("What Pokemon do you choose? (Name/ID) ")
    pokemon = get_pokemon(pokemon_name)
    print('   -------------------------')
    print('|                           |')
    print('|   You chose {}!          '.format(pokemon['name']))
    print('|                           |')
    print('   ------------------------- ')

    # Pause for dramatic effect....
    time.sleep(1)
    print(' ----------------------------------------------')
    print('|     {}\'s stats are:                           '.format(pokemon['name']))
    print('|          hp: {}                                |'.format(pokemon['hp']))
    print('|          attack: {}                            |'.format(pokemon['attack']))
    print('|          defence: {}                           |'.format(pokemon['defence']))
    print('|          speed: {}                             |'.format(pokemon['speed']))
    print(' -----------------------------------------------')

    # Choosing Stat
    stat_choice = input('Which stat do you want to use? (hp, attack, defence, speed) ')
    my_stat = pokemon[stat_choice]
    print(f"{pokemon['name']}\'s {stat_choice} is {my_stat}")

    # Opponents random pokemon
    opponent_pokemon = random_pokemon()
    print(' --------------------------------------- ')
    print('|                                       |')
    print('|    The opponent chose {}'.format(opponent_pokemon['name']))
    print('|                                       |')
    print(' ---------------------------------------')

    # Pause for dramatic effect
    time.sleep(2)

    # Show your pokemon photo and opponent's pokemon photo
    show_combined_pokemon(pokemon['photo'], opponent_pokemon['photo'])

    # Pause for dramatic effect
    time.sleep(2)

    # Opponents Stat
    opponent_stat = opponent_pokemon[stat_choice]
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f"{opponent_pokemon['name']}\'s {stat_choice} is {opponent_stat}")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    # Result
    if my_stat > opponent_stat:
        print(' ------------------------------')
        print('|                              |')
        print(f'|     {trainer_name} Wins!')
        print('|                              |')
        print(' ------------------------------')
        my_score += 1
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'{trainer_name} : {my_score}')
        print(f'Opponent Score : {opponent_score}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    elif my_stat < opponent_stat:
        print(' -------------------------------')
        print('|                               |')
        print(f'|    {trainer_name} Loses!     ')
        print('|                               |')
        print(' -------------------------------')
        opponent_score += 1
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'{trainer_name} : {my_score}')
        print(f'Opponent Score : {opponent_score}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    else:
        print(' ------------------------- ')
        print('|                         |')
        print('|      It\'s a tie!       |')
        print('|                         |')
        print(' -------------------------')
        opponent_score += 1
        my_score += 1
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'{trainer_name} : {my_score}')
        print(f'Opponent Score : {opponent_score}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    # Breaking Loop and End Game Message
    if my_score == limit or opponent_score == limit:
        if opponent_score > my_score:
            print(f'Sorry {trainer_name}! Your opponent won! :(')
            print('Better Luck Next Time!')
            print(' --------------------------- ')
            print('|                           |')
            print('|        Game Over          |')
            print('|                           |')
            print(' --------------------------- ')
            break
        elif opponent_score < my_score:
            print(f'Good job {trainer_name}! You won! Yay! :)' )
            print(' --------------------------- ')
            print('|                           |')
            print('|        Game Over          |')
            print('|                           |')
            print(' --------------------------- ')
            break
        elif opponent_score == my_score:
            print('It\'s a tie. Looks like both you and your opponent are winners! :)')
            print(' --------------------------- ')
            print('|                           |')
            print('|        Game Over          |')
            print('|                           |')
            print(' --------------------------- ')
            break