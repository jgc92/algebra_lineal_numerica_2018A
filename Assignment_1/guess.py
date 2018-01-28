from ex8_functions import *
import random

i = 1
bingo = random.randint(1,10)

n_guess = guess_game(bingo,1)
print("You got it in: " + str(n_guess) + " times!")
