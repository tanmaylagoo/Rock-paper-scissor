import random

'''1 is for rock
0 is for paper
-1 is for scissors
'''
computer=random.choice([-1,0,1])
you=input("Enter your choice:").lower()

game_dict={"rock":1,
           "paper":0,
           "scissor":-1
           }
rev_dict={1:"rock",
           0:"paper",
           -1:"scissor"
           }
num=game_dict[you]
print(f"You chose {rev_dict[num]} \nComputer chose {rev_dict[computer]}\nTherefore,")
if (computer-num==1 or computer-num==-2):
    print("You win!")
if (computer==num):
    print("Tie!")
else:
    print("You lose!")

'''if computer==num:
    print("Tie")
else:
    if (computer==0 and num==1): 
        print("You Lose!")
    elif (computer==0 and num==-1):
        print("You Win!")
    elif (computer==1 and num==0):
        print("You Win!")
    elif (computer==1 and num==-1):
        print("You Lose!")
    elif (computer==-1 and num==0):
        print("You Lose!")
    elif (computer==-1 and num==1):
        print("You Win!")
    else:
        print("Something went wrong!")'''

