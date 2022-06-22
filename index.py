import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&*")

#Create a new password

def generate_new_password():
  length = int(input("Enter password length: "))
	
  random.shuffle(characters)
  password = []
  for i in range(length):
    password.append(random.choice(characters))
  random.shuffle(password)
  print("".join(password))

# UI

def start():
  print("1. Generate New Random Password \n 2. Save New Password \n 3. Retrieve Saved Password \n 4. Exit")
  task = input("Which would you like? ")

  if task == "1":
    generate_new_password()
  else:
    print("beans")

start()