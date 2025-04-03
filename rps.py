import random

'''1 is for rock
0 is for paper
-1 is for scissors
'''
computer = random.choice([-1, 0, 1])
you = input("Enter your choice (rock, paper, scissor): ").lower()

game_dict = {"rock": 1, "paper": 0, "scissor": -1}
rev_dict = {1: "rock", 0: "paper", -1: "scissor"}

if you not in game_dict:
    print("Invalid choice! Please enter rock, paper, or scissor.")
else:
    num = game_dict[you]
    print(f"You chose {rev_dict[num]} \nComputer chose {rev_dict[computer]}\nTherefore,")

    if num == computer:
        print("Tie!")
    elif (computer - num == 1) or (computer - num == -2):
        print("You win!")
    else:
        print("You lose!")
