friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]

# for i in range(len(friends)):  # well you should use for each loop instead for loop. and it will be looked like 'for friend in friends:'
#     if friends[i] == "James":  # If friend name is James you should not do anything so just continue iteration for example
#         print(friends[i], "we are the best friends")
#     elif friends[i] in enemies:
#         print(friends[i], "we are not the friends anymore")
#     else:
#         print(friends[i], "we are the best friends")

# Good but make some changes. Take a look on f string instead of calling print with several parameters

for i in friends:
    if i == "James":
        break
    elif i in enemies:
        print(f"{i} we are not the friends anymore")
    else:
        print(f"{i} we are the best friends")
