import requests, time, random, os, sys

def get_pokemon_names(file_name='pokemon_chars.txt'):
    url = "https://pokeapi.co/api/v2/pokemon"
    
    with open(file_name, 'w') as file:
        while url:
            response = requests.get(url)
            data = response.json()
            for pokemon in data['results']:
                file.write(pokemon['name'] + '\n')
                print(pokemon['name'])
            url = data['next']
            time.sleep(1)
    print("====================================")
    time.sleep(5)
    print("\nFinished retrieving pokemon names.")
    time.sleep(5)

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
    if response.status_code == 404:
        return None
    data = response.json()
    return data

def display_pokemon_info(data):
    abilities = data['abilities']
    stats = data['stats']
    forms = data['forms']
    moves = data['moves']
    species = data['species']['name'].capitalize()

    print(f"\nID No.: {data['id']}")
    print(f"Height: {data['height']}")
    print(f"Weight: {data['weight']}")
    print(f"Species: {species}")
    print(f"Base Experience: {data['base_experience']}")

    print("\nStats:")
    for stat in stats:
        print(f"  {stat['stat']['name'].capitalize()}: {stat['base_stat']}")

    print("\nAbilities:")
    for ability in abilities:
        print(f"  - {ability['ability']['name'].capitalize()}")

    print("\nForms:")
    for form in forms:
        print(f"  - {form['name'].capitalize()}")

    print("\nMoves:")
    for move in moves:
        print(f"  - {move['move']['name'].capitalize()}")

def get_pokemon_info():
    if not os.path.exists('pokemon_chars.txt'):
        print("\nRetrieving pokemon names... Please wait!")
        time.sleep(5)
        get_pokemon_names()

    get_random_pokemon = input('\nGet random pokemon character? (type "yes" or "no"): ').strip().lower()

    if get_random_pokemon == "no":
        pokemon_name = input('\nName of pokemon character? ').strip()
        data = fetch_pokemon_data(pokemon_name)
        if data is None:
            print(f"\nError 404: The pokemon '{pokemon_name}' does not exist.")
            return get_pokemon_info()
    elif get_random_pokemon == "yes":
        with open('pokemon_chars.txt', 'r') as file:
            names = file.readlines()
        pokemon_name = random.choice(names).strip()
        data = fetch_pokemon_data(pokemon_name)
    else:
        print("Invalid input, type yes or no.")
        return get_pokemon_info()
    
    print('\n==========================')
    print(" " + pokemon_name.capitalize())
    print('==========================')
    display_pokemon_info(data)

    time.sleep(3)

    get_new_pokemon = input('\nGet new pokemon character? (type "yes" or "no"): ').strip().lower()
    if get_new_pokemon == "no":
        print("\nGoodbye!")
        sys.exit()
    elif get_new_pokemon == "yes":
        return get_pokemon_info()
    else:
        print("Invalid input, type yes or no.")
        return get_pokemon_info()

get_pokemon_info()
