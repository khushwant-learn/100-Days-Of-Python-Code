# Rock Paper Scissor

import random

r = '''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_choice = input("Choose your weapon (R for Rock, P for Paper, S for Scissor) ").lower()

'''
if user_choice == 'r'   user_choice = r
elif user_choice == 's' 
'''

user_choice = r if user_choice == 'r' else (p if user_choice == 'p' else (s if user_choice == 's' else 'invalid choice'))

#user_choice_dict = {'r' : r, 'p' : s, 's' : s}

# To choose a computer's weapon
rand_choice = random.randint(0,2)
if rand_choice == 0:
    comp_choice = r
elif rand_choice == 1:
    comp_choice = p
else:
    comp_choice = s


if user_choice == comp_choice:
    result = 'draw'

elif (user_choice == 'r' and comp_choice =='s') or (user_choice == 'p' and comp_choice == 'r') or (user_choice == 's' and comp_choice == 'p'):
    result = 'user won'

else:
    result = 'comp win'

print(f'User Choice :  {user_choice}')
print('Comp Choice :  ', comp_choice)
print(result)

