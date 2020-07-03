import random
print("WELCOME TO ROCK PAPER SCISSOR GAME\n")
lst = ["Rock", "Paper", "Scissor"]
computer_score = 0
player_score = 0
game = 0
chance = 6
while game < chance:
    choice = random.choice(lst)
    turn = input("choose(rock, paper or scissor) : ").lower()
    game +=1
    if turn == "rock" and choice == "Scissor":
        print("Computer's point\n")
        computer_score += 1
    if turn == "rock" and choice == "Paper":
        print("Player's point\n")
        player_score += 1
    if turn == "rock" and choice == "Rock":
        print("No points\n")

    elif turn == "paper" and choice == "Scissor":
        print("Computer's point\n")
        computer_score += 1
    elif turn == "paper" and choice == "Rock":
        print("Player's point\n")
        player_score += 1
    elif turn == "paper" and choice == "Paper":
        print("No points\n")

    elif turn == "scissor" and choice == "Rock":
        print("Computer's Point\n")
        computer_score += 1
    elif turn == "scissor" and choice == "Paper":
        print("Player's point\n")
        player_score += 1
    elif turn == "scissor" and choice == "Scissor":
        print("No points\n")
        break


print(f'Computer score: {computer_score}\n')
print(f'Player score : {player_score}\n')


if computer_score > player_score:
    print("computer win")
elif computer_score < player_score:
    print("you win")
else:
       print("Nobody win")
input()



