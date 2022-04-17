# 1
toshiba = ['Kara Cohen', 'Onur Boyce', 'Cindy Brooks', 'Saarah Lowe']
global_logic = ['Cindy Brooks', 'Arif Perkins', 'Ryan Ferry']

toshiba.extend(global_logic)
global_logic.clear()

# print(f"Global logic employees: {global_logic}")
# print(f"Toshiba employees: {toshiba}")

# Good but employees of global now in both companies but should be in toshiba
# Fixed

# 2
bingo_blacklist = {'Riccardo Lozano', 'Nicky Powell', 'Randy Morris'}
poker_blacklist = {'Mila Salter', 'Randy Morris', 'Abel Poole', 'Jem Chase'}
mahjong_blacklist = {'Randy Morris', 'Riccardo Lozano', 'Gruffydd Vaughan'}

bingo_blacklist.intersection(poker_blacklist, mahjong_blacklist)
# Good

# 3
vegetarians = ['Brian Hunter', 'Osman Leon', 'Nikhil Owens']
omnivores = ['Eben Tyson', 'Nico White', 'Darius West', 'Delia Owen']

print(vegetarians + omnivores)

# Good

# 4
vip_places = {
    'place_1': 'Carl Ho',
    'place_2': 'Alexie Cardenas',
    'place_3': 'Martina Carpenter',
    'place_4': 'Alix Rooney',
    'place_5': 'Tyrese Pena',
    'place_6': 'Intruder',
}
common_places = {
    'place_1': 'Keeleigh Craig',
    'place_2': '',
    'place_3': 'Hamid Ford',
    'place_4': 'Cairo Lugo',
    'place_5': 'Emeli Hunt',
    'place_6': '',
    'place_7': 'Mya Iles',
    'place_8': '',
    'place_9': 'Anne Cano'
}


# Not bad but I can easily extend vip places
# I have no idea how to make

# 5
people = [
    'Rahim Mccoy', 'John Dow', 'Dorothy King', 'Khalil Olson',
    'Marta Dow', 'John Dow', 'Leyton Brandt', 'Dorothy King'
]

for i in people:
    if people.count(i) > 1:
        people.remove(i)
print(people)

# Interesting solutions. take a look how it could be implemented in one string
# print(list({}.fromkeys(list_of_guests).keys()))

# Move all tasks in separate modules
