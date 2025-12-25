'''*** Word guessing Game ***'''

import random

user_name= input('Enter Your Name: ').upper();print()
print(f'                            HELLO {user_name}!!!\n                   WELCOME TO THE WORD GUESSING GAME...');print()
print('WORDS ARE: ');print(end= '   ')

words= ['ambiguous','conscientious','inevitable','meticulous','notorious',
        'obsolete','paradox','resilient','superficial','vulnerable']

print(words);print()
print('                     GUESS THE WORD WITHIN LIMITED TURNS...\n                            GOOD LUCK!!!');print()
print('Meaning:',end=' ')
secret_word= random.choice(words)
if secret_word=='ambiguous':
    print("When something is not clear and people understand it in different ways.")
elif secret_word=='conscientious':
    print("A person who does their work properly and cares about doing it right. ")
elif secret_word=='inevitable':
    print("Something that will happen no matter what.")
elif secret_word=='meticulous':
    print("Someone who is extremely careful, even with small things.")
elif secret_word=='notorious':
    print("Famous for bad things, not good ones.")
elif secret_word=='obsolete':
    print("Too old to use now because better things exist.")
elif secret_word=='paradox':
    print("Something that sounds wrong, but is actually true.")
elif secret_word=='resilient':
    print("Able to be strong again after problems.")
elif secret_word=='superficial':
    print("Only looks at the outside, not the real meaning.")
else:
    print("Easy to hurt or get harmed.")
print()

length_secret_word= len(secret_word) # get the length of secret word
turns= length_secret_word + 3       # only give three additional turn to guess the word

# now we have to make the part that get letters and match them with secret word
letter_list= []
index_list= []
c= length_secret_word
for i in range(turns):
    turns-= 1
    letter= input('Enter a letter: ').lower()
    if letter in secret_word:
        letter_list.append(letter)
    else:
        print('Invalid letter')
    
    if length_secret_word == len(letter_list):
        print('you have guessed the word.')
        print(f"The word is {secret_word}")
        break
    else:
        print()
        print(f'You have {turns} to guess the word.')
print('End')
