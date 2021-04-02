import random
from getPokemon import get_pokemon


def random_pokemon():
    pokemon_number = random.randint(1, 151)

    return get_pokemon(pokemon_number)
