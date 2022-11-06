import requests
import pprint as pp

name_or_id = input("dime: ")  # name
#name_or_id = 1         # id

url = "https://pokeapi.co/api/v2/pokemon/{}/".format(name_or_id)

response = requests.get(url)

if response.status_code != 200: 
    print(response.text)
else:
    data = response.json()
  
    print('\n--- language : name ---\n')
    names = []
    for item in data["abilities"]:
        print(item['ability']['name'],":", item['ability']['url'])
        
    print('\n--- language : name ---\n')
    names = {}
    for item in data["sprites"]:
        print(item[(1)])

