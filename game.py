
# console.writeline
import random

print("This is the guessing game")
print()


the_number = random.randint(0, 100)
guess_text = input("What number am I thinking of [0, 100]? ")

print(type(guess_text))
guess = int(guess_text)

while guess != the_number:
    if guess > the_number:
        print("Too high")
    elif guess < the_number:
        print("Too low")
    else:
        break
    guess_text = input("What number am I thinking of [0, 100]? ")

    guess = int(guess_text)

print("Right it was {0}".format(guess))
print("Done!")
