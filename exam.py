patient = "John Smith"
age = 20
is_new = True

age = input("John,How old are you? ")
print(f"You are {age} years old.")

birth_year = int(input("Enter your birth year: "))
age = 2025 - birth_year
print(age)


course = 'Python for Beginners'
print(course.upper())
print(course)

course.lower()
print(course.lower())

print(course.replace('Beginners', 'Absolute Beginners'))

#IF Statements
temperature = 25
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("Its a nice day")
elif temperature > 10:
    print("Its a cold day")
else:
    print("Its cold")

#while loops
i = 1
while i <= 10:
    print(i)
    i = i + 1

i = 1
while i <= 10:
    print(i * '*')
    i = i + 1

i = 100
while i >= 1:
    print(i)
    i= i - 1

# Lists
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[0])
print(names[-1])
print(names[2:4])
names[0] = 'Jon'
print(names)



