# Day 7 - Hangman

## What I Built

A CLI Hangman game that picks a random word from a list, lets the user guess one letter at a time, tracks lives, and displays an ASCII hangman figure that progressively fills in as wrong guesses are made.

## Concepts Used

- `import random` — access Python's random module for word selection
- `random.choice(list)` — pick one random item from a list
- `list.append()` — add correctly guessed letters to a tracker list
- `in` operator — check if a letter is already guessed or exists in the word
- `for` loop over a string — iterate character by character through the chosen word to build the display
- String concatenation (`+=`) — build the `new_display` string one character at a time
- `"_" not in display` — detect win condition by checking if all blanks are filled
- `stages[lives]` — index into a list using a variable to show the correct hangman stage
- Multi-line strings (`"""..."""`) — store the logo and ASCII art stages as readable blocks

## Code

```python
import random

word_list = ["apple", "banana", "mango", "grape", "peach"]

logo = """
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |
                   |___/
"""

stages = [
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """,
    # ... (full stages list)
]

lives = 6
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = "_" * word_length
print("Word to guess:", display)

game_over = False
correct_letters = []

while not game_over:
    print(f"\n****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    new_display = ""

    for letter in chosen_word:
        if letter == guess:
            new_display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print("Word to guess:", display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"\nIT WAS {chosen_word}! YOU LOSE")

    if "_" not in display:
        game_over = True
        print("\nYOU WIN")

    print(stages[lives])
```

## Sample Output

```
[Hangman ASCII logo]

Word to guess: _____

****************************6/6 LIVES LEFT****************************
Guess a letter: a
Word to guess: a___a

****************************6/6 LIVES LEFT****************************
Guess a letter: z
You guessed z, that's not in the word. You lose a life.
Word to guess: a___a

     -----
     |   |
     O   |
         |
         |
         |
    --------

****************************5/6 LIVES LEFT****************************
Guess a letter: n
Word to guess: ana__a
...
YOU WIN
```

## What I Learned

- `stages[lives]` is an elegant way to sync the ASCII art to game state — as `lives` decreases, you naturally move forward through the list without any extra index variable
- Building `new_display` from scratch on every loop iteration (rather than modifying the old one) is the clean approach — it correctly handles the case where a new guess reveals multiple positions of the same letter at once
- The `correct_letters` list does double duty: it prevents the display from "forgetting" previous correct guesses, and it lets you detect duplicate guesses before processing
- `"_" not in display` is a neat win-condition check — once every blank is filled, the game ends without needing a separate counter
- Storing ASCII art frames in a list indexed by remaining lives is a simple but satisfying way to manage multi-state visuals without any `if/elif` chains
