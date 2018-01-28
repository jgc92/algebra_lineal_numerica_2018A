import random

def guess_game(n,i):
    while True:
        guess = input("Guess the number: \n")
        guess = int(guess)
        count = i

        if guess != n:
            count += 1
            print("Wrong! Guess again \n")
            return guess_game(n,count)
        else:
            print("Correct!!!")
            return count

i = 1
bingo = random.randint(1,10)

n_guess = guess_game(bingo,1)
print("You got it in: " + str(n_guess) + " times")
