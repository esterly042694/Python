#Python Password cracker
#Benjamin T. Esterly
#11 October 2018
#Keesler AFB, Biloxi MS

import itertools
import string

def guess_password(real,space):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(space-1,space+1):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            print(guess, attempts)

			

pas = input('Please enter a password : ')
num = len(pas)

print(guess_password(pas,num))

import os
os.system("pause")