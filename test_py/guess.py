import random as randomlib
random = randomlib.randint(1, 100)
print("Guess a number between 1 and 100")
while True:
    guess = int(input())
    if guess < random:
        print("Too low")
    elif guess > random:
        print("Too high")
    else:
        print("That's right!")
        break