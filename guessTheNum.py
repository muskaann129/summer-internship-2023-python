import random

a = int(input("Guess a number between 1-10: "))
guess = random.randint(1,10)

while True:
    if a>100:
        print("Invalid input")
        break

if a==guess:
    print("You guessed it right!")
else:
    print("Wrong guess!")