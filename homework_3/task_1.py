elements = [1, 2, 3, 4, 5, 6, 7, 8]  # We already know that it is a list so I suggest to name it like elements
even_elements = []  # Same. I suggest to name it like event_elements
odd_elements = []  # Same. I suggest to name it like odd elements

for index, value in enumerate(elements):
  if index % 2 == 0:
    even_elements.append([index, value])
  else:
    odd_elements.append([index, value])

# for i in range(0, len(list_of_all), 2):
#   list_of_even += (i, list_of_all[i])  # it chould be list of tuples but you have create simple list
#
# for i in range(0, len(list_of_all), 2):
#   list_of_odd.extend([i, list_of_all[i+1]])

print(even_elements)
print(odd_elements)

# Well. Something was done in this task but incorectly. Take a look on last link for lesson 3.
# TODO: rewrite task using single for each loop. You have used for loop instead.
# TOOD: you should create list of tuples. You have make list and I don't understand which fron elements index and which one is element
# Some examples of how to make list of tuples:
# some_list.append((index, value))

# Some examples of how to determine is element even or odd:
# if index % 2 == 0:
#     print("element is event")
# else:
#     print("element is odd")

# Also I suggest to look on list of links which I have provide for lesson and take a look on enumarate function
