import requests
from PIL import Image


def show_combined_pokemon(your_photo_url, opponent_photo_url):
    your_pokemon = Image.open(requests.get(your_photo_url, stream=True).raw)
    opponent_pokemon = Image.open(requests.get(opponent_photo_url, stream=True).raw)
    combined_image = Image.new('RGBA', (your_pokemon.width + opponent_pokemon.width, your_pokemon.height))
    combined_image.paste(your_pokemon, (0, 0))
    combined_image.paste(opponent_pokemon, (your_pokemon.width, 0))
    combined_image.show()
