# Python Guess Game

Welcome to the **Python Guess Game!** This fun game challenges you to beat the high score by generating a random score each time you play. If you score higher than the current high score, you set a new `record!`

## Table of Contents:

- ### Features
- ### Installation
- ### Usage
- ### How It Works
- ### Future Improvements

## Features:

- **Random Score Generation:**  Each round, the game generates a random score between 1 and 1000.
  
- **High Score Tracking:**  The highest score is saved in main.txt and updated whenever a new high score is achieved.
  
- **Replay Option:**  After each round, players can choose to play again or exit the game.
  
- **File Handling & Error Handling:**  The game handles file reading and writing operations gracefully, ensuring a seamless experience.

## Installation

### Clone the repository:
   
    git clone https://github.com/your-username/python_guess_game.git

### Navigate to the directory:

    cd python_guess_game

### Ensure you have `Python 3.x` installed.

## Usage:

1. Run the game with the following command: python guess_game.py

2. Follow the on-screen prompts to play the game. You’ll see your score, and if it's higher than the high score, it will be saved as the new high score.


How It Works
Generating a Random Score: The play_game() function generates a score between 1 and 1000 using Python's random module.
Retrieving High Score: The get_high_score() function reads the high score from main.txt if it exists. If the file is missing or contains invalid data, the high score defaults to 0.
Saving High Score: When a new high score is achieved, the save_high_score() function updates main.txt with the new score.
Game Loop: The main() function allows players to replay the game, asking them if they want to play another round or exit.
Future Improvements
Custom Scoring Range: Allow players to set their preferred range for random scores.
Leaderboard: Implement a leaderboard to display multiple high scores.
User Profiles: Allow different users to maintain separate high scores.
Enjoy playing the Python Guess Game and see if you can beat the high score!
