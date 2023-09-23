import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (stone, paper, scissors): ").lower()
        if user_choice in ['stone', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose again.")

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_wins = 0
    computer_wins = 0
    rounds = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}. The computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_wins += 1
        elif "lose" in result:
            computer_wins += 1

        rounds += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"\nTotal Rounds: {rounds}")
    print(f"You won {user_wins} times.")
    print(f"The computer won {computer_wins} times.")

play_game()
