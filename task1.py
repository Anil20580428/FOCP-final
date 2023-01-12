import random

FRUITS = ['guava', 'apple', 'bannana', 'grape', 'blueberry']
COLORS = ['teal', 'gray', 'orange', 'navy', 'blue']
ANIMALS = ['camel', 'gorilla', 'snake', 'kangaroo']

def generate_password():
  fruits = random.choice(FRUITS)
  color = random.choice(COLORS)
  animal = random.choice(ANIMALS)

  # Here we create passwords by adding three variables or lists
  password = fruits + color + animal

  return password

#Here we take input from user and errors handelling
while True:
  try:
    inpt = int(input("Password Generator\n==================\nHow many passwords are needed?: "))
    if inpt < 1 or inpt > 24:
      print("Please enter a value between 1 and 24.")
      continue
    break
  except ValueError:
    print("Please enter a number.")

# Generating passwords
passwords = []
for i in range(inpt):
  password = generate_password()
  passwords.append(password)

#Print
print()
for i, password in enumerate(passwords):
    #Here in first {} we put serial number and in second {} we put generated passwords
  print("  {} --> {}".format(i+1, password))