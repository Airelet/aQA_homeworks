# 1
toshiba = ['Kara Cohen', 'Onur Boyce', 'Cindy Brooks', 'Saarah Lowe']
global_logic = ['Cindy Brooks', 'Arif Perkins', 'Ryan Ferry']

toshiba.extend(global_logic)

# 2
bingo_blacklist = {'Riccardo Lozano', 'Nicky Powell', 'Randy Morris'}
poker_blacklist = {'Mila Salter', 'Randy Morris', 'Abel Poole', 'Jem Chase'}
mahjong_blacklist = {'Randy Morris', 'Riccardo Lozano', 'Gruffydd Vaughan'}

bingo_blacklist.intersection(poker_blacklist, mahjong_blacklist)

# 3
vegetarians = ['Brian Hunter', 'Osman Leon', 'Nikhil Owens']
omnivores = ['Eben Tyson', 'Nico White', 'Darius West', 'Delia Owen']

print(vegetarians + omnivores)
