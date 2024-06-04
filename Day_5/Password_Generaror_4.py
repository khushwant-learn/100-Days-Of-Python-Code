import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_letters = []
for i in range(nr_letters):
    password_letters.append(random.choice(letters))

password_symbols = []
for i in range(nr_symbols):
    password_symbols.append(random.choice(symbols))

password_numbers =[]
for i in range(nr_numbers):
    password_numbers.append(random.choice(numbers))

password = password_letters + password_symbols + password_numbers

password_shuffled = []  # Defining a list to contain characters for final shuffled password
indices_occured = []    # Defining a list to contain random indices which occured
i = 0   # initialize i 
while (i < len(password)):  # Loop to iterate the number of characters in password list
    random_index = random.randint(0, len(password) - 1) # a random index from password list
    if (random_index not in indices_occured):   # random number is not in previously occured random numbers
        password_shuffled.append(password[random_index])    # Append the character(element) from the password list at random index which occured, to the shuffled password list
        indices_occured.append(random_index)    # Append that random number to the indices_occured list, so that next time if the same random number occured we can ignore that by checking in this list
        i += 1  # Increase i by 1 only in case of password_shuffled appended a character from password

password_shuffled_string = ''.join(password_shuffled) # To convert the list of characters to a 'string'
print(password_shuffled_string)