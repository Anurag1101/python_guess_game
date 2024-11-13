import random
import os

def get_high_score(file_path):
    # Check if the high score file exists
    if not os.path.exists(file_path):
        return 0  # Return 0 if file does not exist

    try:
        with open(file_path, "r") as f:
            highscore = f.read()
            return int(highscore) if highscore.isdigit() else 0
    except ValueError:
        return 0  # Return 0 if there was an error reading an integer

def save_high_score(file_path, score):
    with open(file_path, "w") as f:
        f.write(str(score))

def play_game():
    print("Welcome to the game!")
    score = random.randint(1, 1000)
    print(f"Your score is: {score}")
    file_path = "main.txt"
    highscore = get_high_score(file_path)

    if score > highscore:
        print("Congratulations! You have a new high score!")
        save_high_score(file_path, score)
    else:
        print(f"The current high score is {highscore}. Try to beat it!")

def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
