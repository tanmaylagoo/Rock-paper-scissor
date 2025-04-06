import random

'''
1 → rock
0 → paper
-1 → scissor
'''

rev_dict = {1: "rock", 0: "paper", -1: "scissor"}

try:
    you = int(input("Enter your choice (1 for rock, 0 for paper, -1 for scissor): "))
    if you not in [-1, 0, 1]:
        print("Invalid choice! Please enter 1, 0, or -1.")
    else:
        computer = random.choice([-1, 0, 1])
        print(f"You chose {rev_dict[you]} \nComputer chose {rev_dict[computer]}\nTherefore,")

        if you == computer:
            print("Tie!")
        elif (computer - you == 1) or (computer - you == -2):
            print("You win!")
        else:
            print("You lose!")
except ValueError:
    print("Invalid input! Please enter a number (1, 0, or -1).")
