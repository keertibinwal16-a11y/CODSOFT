import random

print("===== ROCK PAPER SCISSORS GAME =====")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user = input("Enter rock, paper, or scissors: ").lower()
    
    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
