# 📘 Assignment: Hangman Game in Python

## 🎯 Objective

Build a command-line Hangman game that uses loops, conditionals, strings, and user input. By the end of this assignment, you will create a complete game flow from word selection to win/lose results.

## 📝 Tasks

### 🛠️	Set Up the Hidden Word and Display

#### Description
Create the starting game setup: choose a random word from a predefined list and display the hidden word to the player using underscores.

#### Requirements
Completed program should:

- Store at least 5 possible words in a Python list.
- Randomly select one word at the start of the game.
- Display progress using underscores for unknown letters (example: `_ _ _ _`).
- Keep track of guessed letters so repeated guesses can be handled.
- Show the current progress after each guess.


### 🛠️	Build the Guessing Loop and Game Outcome

#### Description
Add the main game loop where the player guesses one letter at a time until they either reveal the full word or run out of incorrect attempts.

Example interaction:
```text
Word: _ _ _ _ _
Guess a letter: a
Good guess!
Word: _ a _ _ a
Attempts left: 5
```

#### Requirements
Completed program should:

- Accept one-letter input from the user each turn.
- Decrease remaining attempts only when the guessed letter is not in the word.
- End the game with a win message when all letters are guessed.
- End the game with a lose message when attempts reach 0, and reveal the word.
- Include clear output each turn: current word progress, guessed letters, and attempts remaining.
- Save your solution in `starter-code.py` and submit that file.
