# 1
john_salary = 1850.0
marta_salary = 2900.0

print(john_salary)
print(marta_salary)

# 2
john_age = 33
marta_age = 42

print(john_age)
print(marta_age)

# 3
john_name = "John Setter"
marta_name = "Marta Lee"

print(john_name)
print(marta_name)

# 4
john_gender = True
marta_gender = False

print(john_gender)
print(marta_gender)

# 5
john_friends = ['Sam', 'Lilly', 'Eren']
marta_friends = ['Sasha', 'Rainer', 'Levi']

# 6
other_people = ['Terry', 'David', 'Terry', 'Sam', 'Kevin', 'Laura', 'Kelly', 'Sam']
other_people = set(other_people)

# 7
john_coordinates = (49.99496221562471, 36.24521026647598)
marta_coordinates = (50.449011010824115, 30.51858206766452)

# 8*
terry = {'full_name': 'Terry Smith',
        'age': 25,
        'salary': 7500.0,
        'gender': False,
        'friends': ['John', 'Merry', 'John', 'John', 'Marta', 'Sam', 'John'],
        'coordinates': (50.020755743304406, 36.366243742621265)
        }
lui = {'full_name': 'Lui Tailor',
        'age': 27,
        'salary': 6880.0,
        'gender': False,
        'friends': ['Merry', 'Merry', 'Lui', 'Don'],
        'coordinates': (48.85303700043509, 2.4566971651495937)
       }
sara = {'full_name': 'Sara Tailor',
        'age': 30,
        'salary': 3500.0,
        'gender': True,
        'friends': ['John', 'Lenny', 'Mark', 'John'],
        'coordinates': (48.85303700043509, 2.4566971651495937)
        }
dan = {'full_name': 'Dan Bi',
        'age': 21,
        'salary': 1200.0,
        'gender': False,
        'friends': ['Mimi', 'Chul', 'Merry', 'Sara'],
        'coordinates': (37.48519619322381, 127.05457171791853)
       }

john_friends.append({'Terry': terry})
john_friends.append({'Lui': lui})
marta_friends.append({'Sara': sara})
marta_friends.append({'Dan': dan})

# 8
john = {'full_name': john_name,
        'age': john_age,
        'salary': john_salary,
        'gender': john_gender,
        'friends': john_friends,
        'coordinates': john_coordinates
        }
marta = {'full_name': marta_name,
        'age': marta_age,
        'salary': marta_salary,
        'gender': marta_gender,
        'friends': marta_friends,
        'coordinates': marta_coordinates
        }

for key, value in john.items():
    print(key, value, sep=" => ")
for key, value in marta.items():
    print(key, value, sep=" => ")

