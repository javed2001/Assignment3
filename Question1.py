import random


def gues_the_number(secret_number):  # Note the typo: 'gues' instead of 'guess'
    atempts = 0  # Typo: 'atempts' instead of 'attempts'
    while True:
        gues = int(input("Gues a number between 100 and 250: "))  # Typo: 'Gues' instead of 'Guess'
        atempts += 1  # Typo: 'atempts' instead of 'attempts'

        if gues < secret_number:
            print("To low!")  # Typo: 'To' instead of 'Too'
        elif gues > secret_number:
            print("To hgh!")  # Typo: 'To' instead of 'Too', 'hgh' instead of 'high'
        else:
            print(
                f"Congratulation! You guesed the secret number {secret_number} in {atempts} atempts.")  # Typo: 'Congratulation', 'guesed', 'atempts'
            break


def main():
    lower_range = 100
    upper_range = 250
    secret_number = random.randint(lower_range, upper_range)

    print("Welcom to the Gues the Number game!")  # Typo: 'Welcom', 'Gues'
    print(f"I'm thinking of a number betwen {lower_range} and {upper_range}.")  # Typo: 'betwen'
    gues_the_number(secret_number)  # Typo: 'gues_the_number'


if __name__ == "__main__":
    main()
