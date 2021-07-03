# 1
list_of_all = [1, 2, 3, 4, 5, 6, 7, 8]
list_of_even = []
list_of_odd = []

for i in range(0, len(list_of_all), 2):
  list_of_even += (i, list_of_all[i])

for i in range(0, len(list_of_all), 2):
  list_of_odd.extend([i, list_of_all[i+1]])

print(list_of_even)
print(list_of_odd)

# 2
two = 2
two_mult_1 = two * 2
two_diff_1 = two / 2
two_mult_2 = two ** 2
two_diff_2 = two // 2

# 3
friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]

for i in range(len(friends)):
  if friends[i] == "James":
    print(friends[i], "we are the best friends")
  elif friends[i] in enemies:
    print(friends[i], "we are not the friends anymore")
  else:
    print(friends[i], "we are the best friends")