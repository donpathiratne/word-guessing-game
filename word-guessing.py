'''*** Word guessing Game ***'''

import random

user_name= input('Enter Your Name: ').upper()
print(f'HELLO {user_name}\nWELCOME TO THE WORD GUESSING GAME...')
print('YOU HAVE BEEN GIVEN SOME WORDS.');print()

words= ['ambiguous','conscientious','inevitable','meticulous','notorious',
        'obsolete','paradox','resilient','superficial','vulnerable']

print(words)
print('GUESS THE WORD WITHIN LIMITED TURNS...\nGOOD LUCK!!!');print()
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
    print("Too old to use now because better thigs exist.")
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
turns= length_secret_word +1         # only give one additional turn to guess the word

# now we have to make the part that get letters and match them with secret word
