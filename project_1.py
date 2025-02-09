

# week one project: A programme for a rock, paper, scissors game

import random
options: tuple = ('rock', 'paper', 'scissors')
running = True

while running:
    player = '' # reset the player choice
    while player not in options:
        player = input("enter your choice(rock, paper, scissors): ")
        computer = random.choice(options)

    print(f"player chooses: {player}")
    print(f"computer chooses: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win!")
    elif player == "scissors" and computer == "paper":
        print("you win!")
    else:
        print("you lose!")

    play_again = input ("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes": # if the player does not want to play again
        running = False  

print("Thanks for playing!")


   

    
   
