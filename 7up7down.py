import random
guess = random.randint(2,12)

while True:
    a = int(input("Enter 1 for 7 Up and 2 for 7 Down: "))
    if a>=3 or a<1:
        print("Invalid input")
        continue
    print(f'The number is: {guess}')
    if (guess>=7 and a==1) or (guess<7 and a==2):
        print("You win, the number was 7 up!!")
    else:
        print("You loose, the number was 7 down")

