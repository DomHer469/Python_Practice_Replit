#DESCRIPTION:
# This python code allows two players to play a game of Rock, Paper, Scissors.
# it prompts each player to enter their choice, validates the input, and determines the winner based on the rules of the game.
# also it clears the screen after each input to keep the input a secret until both players have made their choices.
# Rock, Paper, Scissors Game

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_player_choice(player_num):
    while True:
        clear_screen()
        choice = input(f"Player {player_num}, enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            clear_screen()
            return choice
        print("Invalid choice! Please enter rock, paper, or scissors.")

def determine_winner(p1_choice, p2_choice):
    if p1_choice == p2_choice:
        return "Tie!"
    
    winning_moves = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_moves[p1_choice] == p2_choice:
        return "Player 1 wins!"
    return "Player 2 wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    p1_choice = get_player_choice(1)
    p2_choice = get_player_choice(2)
    
    print("\nRevealing choices:")
    print(f"Player 1 chose: {p1_choice}")
    print(f"Player 2 chose: {p2_choice}")
    print("\n" + determine_winner(p1_choice, p2_choice))

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            break

print("Thanks for playing!")