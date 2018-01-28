def guess_game(n: int, i: int) -> int:
    """ Guess game! Asks you for a number until you guess correctly.

        Args:
            n: answer number
            i: count initializer

        Returns:
            Number (int) of times it took the user to guess n.

    """
    
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
