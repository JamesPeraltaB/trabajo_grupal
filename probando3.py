
import webbrowser
def fetch_pokemon():
     name = input('Which Pokemon do you want to fetch? ')
     print("Fetching " + name)
     poke = pokemon(name)
     print(poke.sprites)
     webbrowser.open(poke.sprites.front_default)