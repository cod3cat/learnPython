person1 = "Allen"
person2 = "Michael"
person3 = "John"
person4 = "Ron"

print(f"The list of people in this group is {person1}, {person2}, {person3}, {person4}")

# Using list

person = ["Allen", "Michael", "John", "Ron"]
print(person)

print(person[0])
print(person[-2])
print(person[0:2])
print(person[:2])
print(person[1:])

person.append("Nat")
print(person)
print(person[-1])

person.remove("Nat")
print(person)

person.pop(-1)
print(person)

person.sort()
print(person)