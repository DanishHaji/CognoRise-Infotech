import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "it's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
        return "You Win!"
    else:
        return "Computer Wins!"

def main():
    choice = ['rock', 'paper', 'scissors']
    play_again = True

    while play_again:
        user_choice = input("Enter your choice (rock, paper, scissors):")
        if user_choice not in choice:
            print("Invalid choice. please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choice)
        print("Computer's choice:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again_input = input("Do you want to play again? (yes/no):")
        if play_again_input != 'yes':
            play_again = False

if __name__ == "__main__":
    main()               