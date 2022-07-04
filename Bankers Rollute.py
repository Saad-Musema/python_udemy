import random

names_string = input("Give me everybody's name, separated by a comma. ")
names = names_string.split(", ")
# print(names)
payer = random.randint(0, len(names) -1)
print(names[payer])


# print(len(names))
