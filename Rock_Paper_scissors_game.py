import random
from rich import print
from rich.panel import Panel

bold_start = "\033[1m"
bold_end = "\033[0m"

game_instructions = '''\n
[bold black on white]This game is mainly played by two players (In this case, You will be playing against the computer).\n
You are expected to make a selection between the three game options (Rock, Paper, Scissors).\n
The computer will choose select an option from the game options too.\n
This selection is done simultaneously and not one after the other, this is so the other player doesn't make a better choice based on their opponent's choice.
In this game the ***Rock*** defeats or crushes ***Scissors*** when they clash, ***Paper*** defeats or crushes ***Rock*** when they clash, and ***Scissors*** defeats or cuts ***Paper*** when they clash.\n
So, Your selection will clash against that of the computer to determine who wins. If you both make the same selection, then it's a tie.[/bold black on white]
'''
panel = Panel(game_instructions, title="GAME INSTRUCTION.")

def game_options():
    return ['rock', 'paper', 'scissors']

def player_choice(options):
    user_choice = None
    while user_choice not in options:
        user_choice = input(f"Please enter your choice. Choose from one of the options ({', '.join(options)}): ").lower()
        if user_choice not in options:
            print(f"Invalid choice. Please select any of these: {', '.join(options)}")
    return user_choice

def computer_choice(options):
    return random.choice(options)

def rules(your_choice, system_choice):
    if your_choice == system_choice:
        return "It's a tie!"
    elif (your_choice == 'rock' and system_choice == 'scissors') or \
         (your_choice == 'scissors' and system_choice == 'paper') or \
         (your_choice == 'paper' and system_choice == 'rock'):
        return "You win!!"
    else:
        return "Computer wins!"

def play():
    print(panel)

    options = game_options()
    while True:
        # Get choices
        your_choice = player_choice(options)
        system_choice = computer_choice(options)

        # Display choices
        print(f"\nYou chose: {your_choice}")
        print(f"Computer chose: {system_choice}\n")

        # Determine the outcome
        result = rules(your_choice, system_choice)
        print(result)

        # Ask if the user wants to play again
        max_attempts = 4
        attempts = 0
        while attempts < max_attempts:
            replay = input("\nDo you want to play again? (yes/no): ").lower()
            if replay in ('yes', 'no'):
                break
            attempts += 1
            print(f"Invalid response. Please enter 'yes' or 'no'. ({max_attempts - attempts} attempts left)")

        if replay == 'yes':
            print("\nGreat!!! Let's play again!\n")
            continue
        elif replay == 'no':
            print("Thanks for playing! Goodbye!")
            break
        else:
            # User exhausted attempts without a valid answer
            print("\nToo many invalid responses. Exiting the game. Goodbye!")
            break

if __name__ == '__main__':
    play()
