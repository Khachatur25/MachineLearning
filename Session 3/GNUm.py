import random

def GNum():
    a = int(random.random()*20)
    guessed_numbers = []
    tries =int(random.random()* 8)

    print("You have",tries,"tries") 
    
    while tries > 0:

        guess = int(input("Guess the number"))
        if guess == a:
            print("Congratulations! You Win!")
            break
        else:
            print("Invalid guess!")
            tries -= 1
            print("You have",tries,"tries")

            if(guess > a):
                print("Your guess is more than NUM")
            else:
                print("NUM is more than your guess")

GNum()
