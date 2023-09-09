# pick and remove a random name from the list

import random

person = ["Allen", "Michael", "John", "Ron"]
print(f"The input list is {person}")

random_choice = random.choice(person)
print(f"The choice is: {random_choice}")

person.remove(random_choice)
print(f"The new list is {person}"   )