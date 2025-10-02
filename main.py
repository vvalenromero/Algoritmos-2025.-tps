
from superheroes_operations import SuperheroList

superheroes_data = [
    {
        "name": "Kang",
        "alias": "Kang the Conqueror",
        "real_name": "Nathaniel Richards",
        "short_bio": "Kang the Conqueror is a time-traveling warlord who has battled many heroes, especially the Avengers. He is known for his mastery of advanced technology and his ability to manipulate time.",
        "first_appearance": 1964,
        "is_villain": True,
        "house": "Marvel"
    },
    {
        "name": "Hulk",
        "alias": "The Hulk",
        "real_name": "Bruce Banner",
        "short_bio": "Hulk is a gamma-powered superhero with incredible strength and durability. He transforms into a green giant when angered or stressed.",
        "first_appearance": 1962,
        "is_villain": False,
        "house": "Marvel"
    },
    {
        "name": "Iron Man",
        "alias": "Iron Man",
        "real_name": "Tony Stark",
        "short_bio": "A billionaire inventor who built a powered suit of armor to save his life and became a founding Avenger.",
        "first_appearance": 1963,
        "is_villain": False,
        "house": "Marvel"
    },
    {
        "name": "Dr Strange",
        "alias": "Dr Strange",
        "real_name": "Stephen Strange",
        "short_bio": "Once a brilliant but arrogant surgeon, he became the Sorcerer Supreme and protector of Earth from magical threats.",
        "first_appearance": 1963,
        "is_villain": False,
        "house": "DC"  # Incorrectamente listado como DC para demostrar el cambio
    },
    {
        "name": "Wolverine",
        "alias": "Wolverine",
        "real_name": "James 'Logan' Howlett",
        "short_bio": "A mutant with regenerative healing and retractable claws.",
        "first_appearance": 1974,
        "is_villain": False,
        "house": "Marvel"
    },
    {
        "name": "Black Widow",
        "alias": "Natasha Romanoff",
        "real_name": "Natasha Romanoff",
        "short_bio": "Black Widow is a highly trained spy and former assassin with exceptional skills in hand-to-hand combat and espionage.",
        "first_appearance": 1964,
        "is_villain": False,
        "house": "Marvel"
    },
    {
        "name": "Spiderman",
        "alias": "Spiderman",
        "real_name": "Peter Parker",
        "short_bio": "A young man with spider-like abilities who fights crime in New York City wearing his iconic suit.",
        "first_appearance": 1962,
        "is_villain": False,
        "house": "Marvel"
    },
    {
        "name": "Batman",
        "alias": "Batman",
        "real_name": "Bruce Wayne",
        "short_bio": "A billionaire who fights crime in Gotham City using his detective skills and advanced suit with armor.",
        "first_appearance": 1939,
        "is_villain": False,
        "house": "DC"
    },
    {
        "name": "Superman",
        "alias": "Superman",
        "real_name": "Clark Kent",
        "short_bio": "An alien from Krypton with superhuman abilities.",
        "first_appearance": 1938,
        "is_villain": False,
        "house": "DC"
    },
    {
        "name": "Mujer Maravilla",
        "alias": "Wonder Woman",
        "real_name": "Diana Prince",
        "short_bio": "An Amazonian warrior princess with superhuman abilities.",
        "first_appearance": 1941,
        "is_villain": False,
        "house": "DC"
    },
    {
        "name": "Capitana Marvel",
        "alias": "Captain Marvel",
        "real_name": "Carol Danvers",
        "short_bio": "A former Air Force pilot with cosmic powers.",
        "first_appearance": 1968,
        "is_villain": False,
        "house": "Marvel"
    },
    {
        "name": "Flash",
        "alias": "The Flash",
        "real_name": "Barry Allen",
        "short_bio": "The fastest man alive with super speed abilities.",
        "first_appearance": 1956,
        "is_villain": False,
        "house": "DC"
    },
    {
        "name": "Star-Lord",
        "alias": "Star-Lord",
        "real_name": "Peter Quill",
        "short_bio": "Leader of the Guardians of the Galaxy.",
        "first_appearance": 1976,
        "is_villain": False,
        "house": "Marvel"
    },
    {
        "name": "Linterna Verde",
        "alias": "Green Lantern",
        "real_name": "Hal Jordan",
        "short_bio": "A member of the Green Lantern Corps with a power ring.",
        "first_appearance": 1959,
        "is_villain": False,
        "house": "DC"
    }
]


superheroes = SuperheroList(superheroes_data)

print("="*60)
print("ACTIVIDADES CON SUPERHÉROES")
print("="*60)

print("\na. Eliminando a Linterna Verde:")
removed = superheroes.remove_by_name("Linterna Verde")
print(f"   Eliminado: {removed['name'] if removed else 'No encontrado'}")

print("\nb. Año de aparición de Wolverine:")
year = superheroes.get_first_appearance("Wolverine")
print(f"   {year}")

print("\nc. Cambiando casa de Dr. Strange a Marvel:")
changed = superheroes.change_house("Dr Strange", "Marvel")
print(f"   Cambio realizado: {changed}")

print("\nd. Superhéroes con 'traje' o 'armadura' en biografía:")
heroes_with_suit = superheroes.find_by_bio_words("traje", "armadura", "suit", "armor")
for name in heroes_with_suit:
    print(f"   - {name}")

print("\ne. Superhéroes con aparición anterior a 1963:")
early_heroes = superheroes.filter_by_year(1963, '<')
for hero in early_heroes:
    print(f"   - {hero['name']} ({hero['house']}) - {hero['year']}")

print("\nf. Casa de Capitana Marvel y Mujer Maravilla:")
print(f"   Capitana Marvel: {superheroes.get_house('Capitana Marvel')}")
print(f"   Mujer Maravilla: {superheroes.get_house('Mujer Maravilla')}")

print("\ng. Información completa de Flash y Star-Lord:")
flash_info = superheroes.get_hero_info("Flash")
starlord_info = superheroes.get_hero_info("Star-Lord")
print(f"   Flash: {flash_info}")
print(f"   Star-Lord: {starlord_info}")

print("\nh. Superhéroes que comienzan con B, M o S:")
heroes_bms = superheroes.filter_by_initial('B', 'M', 'S')
for name in heroes_bms:
    print(f"   - {name}")

print("\ni. Cantidad de superhéroes por casa:")
count_by_house = superheroes.count_by_house()
for house, count in count_by_house.items():
    print(f"   {house}: {count}")

print("\n" + "="*60)
print("OPERACIONES CON LISTAS")
print("="*60)

lista1 = SuperheroList([
    {"name": "Thor", "house": "Marvel"},
    {"name": "Batman", "house": "DC"},
    {"name": "Hulk", "house": "Marvel"}
])

lista2 = SuperheroList([
    {"name": "Superman", "house": "DC"},
    {"name": "Hulk", "house": "Marvel"},
    {"name": "Flash", "house": "DC"}
])

print("\na. Concatenar dos listas:")
concatenated = lista1.concatenate(lista2)
print(f"   Total elementos: {len(concatenated)}")

print("\nb. Concatenar sin repetidos:")
unique_concat = lista1.concatenate_unique(lista2, key='name')
print(f"   Total elementos únicos: {len(unique_concat)}")
for hero in unique_concat:
    print(f"   - {hero['name']}")

print("\nc. Elementos repetidos entre listas:")
intersection_count = lista1.count_intersection(lista2, key='name')
print(f"   Cantidad de elementos en común: {intersection_count}")

print("\nd. Eliminando todos los elementos de una lista:")
demo_list = SuperheroList([
    {"name": "Demo1"}, 
    {"name": "Demo2"}, 
    {"name": "Demo3"}
])
demo_list.delete_all_showing()