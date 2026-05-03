import random
number = random.randint(1,100)
while True:
    numberofUser=int(input("Guess the number between 1 and 100"))
    if number==numberofUser:
        print("you won ")
        break
    elif numberofUser < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")