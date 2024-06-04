#import Password_Generator
import random

password_letters = ['f', 's', 'u', 'a']
password_symbols = ['@', '*', '#']
password_numbers = ['4', '8', '3']

password = password_letters + password_symbols + password_numbers
print(password)

password_shuffled = password

random.shuffle(password_shuffled)
print(password_shuffled)

password_shuffled_string = ''.join(password_shuffled)
print(password_shuffled_string)