from randomPokemon import random_pokemon
from getPokemon import get_pokemon
from combinePokemonImage import show_combined_pokemon

# Choosing pokemon
pokemon_name = input("What Pokemon do you choose? (Name/ID) ")
pokemon = get_pokemon(pokemon_name)
print('You chose {}'.format(pokemon['name']))

# Choosing Stat
stat_choice = input('Which stat do you want to use? (hp, attack, defence, height, weight) ')
my_stat = pokemon[stat_choice]
print(f"{pokemon['name']}\'s {stat_choice} is {my_stat}")

# Opponents random pokemon
opponent_pokemon = random_pokemon()
print('The opponent chose {}'.format(opponent_pokemon['name']))

# Show your pokemon photo and opponent's pokemon photo
show_combined_pokemon(pokemon['photo-url'], opponent_pokemon['photo-url'])

# Opponents Stat
opponent_stat = opponent_pokemon[stat_choice]
print(f"{opponent_pokemon['name']}\'s {stat_choice} is {opponent_stat}")

# Result
if my_stat > opponent_stat:
    print('You Win!')
elif my_stat < opponent_stat:
    print('You Lose!')
else:
    print('Draw!')
