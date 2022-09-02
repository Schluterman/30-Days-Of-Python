import imp
from random import randint
import sys
answer = randint(int(sys.argv[1],sys.argv[10]))



while True:
    try:
        guess = int(input('guess a number 1 to 10:  '))
        if  0 < guess < 11:
            if guess == answer:
                print('you got it right')
                break
        else:
            print('hey 1 to 10')
    except ValueError:
        print('please enter a number')
        continue