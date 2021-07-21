names = ["John", "Marta", "James", "Amanda", "Marianna"]

for name in names:
    print(f'{name:>15}')

# Good but solved only in 1 way. It could be done also with str rjust method
for name in names:
    print(name.rjust(15, ' '))
