import requests
import pprint as pp

name_or_id = input("dime: ")  # name
#name_or_id = 1         # id

url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{}.png".format(name_or_id)

response = requests.get(url)

print(name_or_id,":", url)