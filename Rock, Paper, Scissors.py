# import random and sys modules
import random
import sys

print('WELCOME TO THE GAME OF ROCK, PAPER, SCISSORS, LIZARD OR SPOCK.')
pick = ["r", "p", "s", "l", "sp"]   # we create a list of the options

# we define the wins, losses and ties at 0
wins = 0
losses = 0
ties = 0

# The main code of the game
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        playerPick = input("Choose your option: (R)ock, (P)aper, (S)cissors, (L)izard, (SP)ock or (Q)uit. ")
        if playerPick == 'q':
            print('Game ended\nFinal score is: %s Wins, %s Losses, %s Ties' % (wins, losses, ties))
            sys.exit()
        if playerPick == 'r' or playerPick == 'p' or playerPick == 's' or playerPick == 'l' or playerPick == 'sp':
            break
        else:
            print('Type one of r, p, s, l, sp or q.')
    computerPick = random.choice(pick)
    print(f"You chose {playerPick} and the computer chose {computerPick}.")
    if playerPick == computerPick:
        print("It's a tie!")
        ties += 1
    elif playerPick == "r":
        if computerPick == "s" or computerPick == "l":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif playerPick == "p":
        if computerPick == "r" or computerPick == "sp":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif playerPick == "s":
        if computerPick == "p" or computerPick == "l":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif playerPick == "l":
        if computerPick == "p" or computerPick == "sp":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif playerPick == "sp":
        if computerPick == "r" or computerPick == "s":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1