import random
# write 'hello world' to the console
print("Hello World")

#create a multiplayer minigame, where a player can choose one of the three options rock, paper, or scissors; the player will play again the computer and the computer can randomly choose one of the elements (rock, paper, or scissors)  for each move, just like the player. Your interaction in the game will be through the console (Terminal).
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.


def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        print("Choose one of the following options: rock, paper, scissors")
        player_choice = input().lower()

        if player_choice not in options:
            print("Invalid option. Please choose again.")
            continue

        computer_choice = random.choice(options)

        print("Player chose:", player_choice)
        print("Computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("Player wins!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print("Player score:", player_score)
        print("Computer score:", computer_score)

        print("Do you want to play again? (yes/no)")
        play_again = input().lower()

        if play_again != 'yes':
            break

    print("Final scores:")
    print("Player score:", player_score)
    print("Computer score:", computer_score)

play_game() 

