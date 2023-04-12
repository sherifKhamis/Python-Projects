# Welcome to a basic Password Generator in Python

import random

# Pool of available signs, letters and numbers
small_letters = "abcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
signs = "^°!§$%&/()=?{[]}\*+~#-_<>|"

# Password length
password_length = int(input("How long do you want your password to be ? "))

# Order and amount of letters, numbers and signs
order = [small_letters, capital_letters, numbers, signs]
random.shuffle(order)  # Shuffled order

first_type_number = random.randint(0, password_length)
second_type_number = random.randint(0, password_length-first_type_number)
third_type_number = random.randint(0, password_length-first_type_number-second_type_number)
fourth_type_number = password_length-first_type_number-second_type_number-third_type_number

first_type = order[0]
second_type = order[1]
third_type = order[2]
fourth_type = order[3]

# for loops for generating actual password
password = ""
for j in range(0, first_type_number):
    password += str(random.choice(first_type))
for k in range(first_type_number, first_type_number+second_type_number):
    password += str(random.choice(second_type))
for l in range(first_type_number+second_type_number, first_type_number+second_type_number+third_type_number):
    password += str(random.choice(third_type))
for m in range(first_type_number+second_type_number+third_type_number, first_type_number+second_type_number+third_type_number+fourth_type_number):
    password += str(random.choice(fourth_type))

# Shuffle generated password to prevent repetition of the same type behind each other
list_password = list(password)
random.shuffle(list_password)
final_password = ""
final_password = final_password.join(list_password)

print(final_password)



