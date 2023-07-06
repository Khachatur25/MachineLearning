import random

def choose_word():
    word_list = ['apple','banana','cherry','durian','elderberry']
    return random.choice(word_list)

def play_hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6

    print("Wellcome To Hangman")

    while tries > 0:
        display_word = ' '
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word: ",display_word)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You Won!")
                break

        else:
            print("Incorrect guess.")
            tries -= 1
            print("Tries remaining: ",tries)

    if tries == 0:
        print("You lost! The word was: ",word)

play_hangman()



