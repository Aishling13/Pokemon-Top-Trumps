import requests


def get_pokemon(pokemon_name):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_name)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'photo': pokemon['sprites']['other']['official-artwork']['front_default'],
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'hp': pokemon['stats'][0]['base_stat'],
        'attack': pokemon['stats'][1]['base_stat'],
        'defence': pokemon['stats'][2]['base_stat'],
        'speed': pokemon['stats'][5]['base_stat']
    }