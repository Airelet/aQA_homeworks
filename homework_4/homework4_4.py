import re

str_cc = ["FirstItem", "FriendsList", "MyTuple"]
str_sc = []

for i in str_cc:
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    i = pattern.sub('_', i).lower()
    str_sc.append(i)

print(str_sc)
