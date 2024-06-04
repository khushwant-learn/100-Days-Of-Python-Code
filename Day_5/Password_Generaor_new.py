import random

password_letters = ['f', 's', 'u', 'a']
password_symbols = ['@', '*', '#']
password_numbers = ['4', '8', '3']

password = password_letters + password_symbols + password_numbers

password = ['f', 's', 'u', 'a', '@', '*', '#', '4', '8', '3']



new_password = []  


previous_random_indices = []

'''
for i in range(10):
    random_index = random.randint(0, 9) 
    new_password.append(password[random_index])
    previous_random_indices.append(random_index)
'''

''' 
while(random_index not in previous_random_indices):
    new_password.append(password[random_index])
    print(new_password)
    previous_random_indices.append(random_index)
    random_index = random.randint(0, 9)
    print(random_index)
''' 

random_index = random.randint(0, 9)
print(random_index)
i = 0
while(i < 10):
    if (random_index not in previous_random_indices):
        new_password.append(password[random_index])
        previous_random_indices.append(random_index)
        i += 1  #increment only in case of appending a character to 'new_password' list

    random_index = random.randint(0, 9)
    
    

print(new_password)

print(''.join(new_password))