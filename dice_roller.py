import random

print(" Welcome to the Dice Roller! ")

# The while loop keeps the program running until we explicitly break out of it
while True:
    # .lower() ensures that if the user types 'Y' or 'N', it still matches our conditions
    choice = input("Roll the dice? (y/n): ").lower()

    if choice == 'y':
        # Generate a random integer between 1 and 6 (inclusive)
        die_roll = random.randint(1, 6)
        print(f"Result: {die_roll}\n")
        
    elif choice == 'n':
        print("Thanks for playing! Goodbye.")
        break # This exits the while loop and ends the program
        
    else:
        print("Invalid input! Please type 'y' to roll or 'n' to quit.\n")