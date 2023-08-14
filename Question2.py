import random

def choose_random_word():
    word_list = ["python", "programming", "hangman", "computer", "algorithm", "developer", "openai", "learning"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def draw_hangman(turns_left):
    hangman_stages = [
        """
         -----
         |   |
             |
             |
             |
             |
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        """
    ]
    print(hangman_stages[6 - turns_left])

def hangman_game():
    word = choose_random_word()
    guessed_letters = []
    turns_left = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while turns_left > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            print(display_word(word, guessed_letters))
            if "_" not in display_word(word, guessed_letters):
                print("Congratulations! You guessed the word!")
                break
        else:
            turns_left -= 1
            draw_hangman(turns_left)
            print(f"Incorrect! You have {turns_left} turns left.")

    if turns_left == 0:
        print("Hangman complete! You lose. The word was:", word)

hangman_game()
