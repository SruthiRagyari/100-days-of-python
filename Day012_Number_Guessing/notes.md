# Day 12 - Number Guessing Game

## What I Built

A CLI number guessing game where the computer picks a random number between 1 and 100, the user chooses a difficulty (easy = 10 tries, hard = 5), and gets feedback after each guess until they win or run out of attempts.

## Concepts Used

- `from random import randint` — import only `randint` from the module instead of the whole `random` namespace
- `randint(1, 100)` — generate a random integer inclusive of both endpoints
- Functions with return values — `check_answer()` returns remaining turns; `set_difficulty()` returns a turn count
- Constants (`EASY_LEVEL_TURNS`, `HARD_LEVEL_TURNS`) — all-caps naming convention for values that never change
- `while guess != answer` — loop that exits on the correct guess or a `return` inside the loop
- Early `return` inside a function — used to exit the game immediately when turns hit 0
- `from art import logo` — importing from a separate local module

## Code

```python
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
```

## Sample Output

```
[Logo]
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Pssst, the correct answer is 47
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again.
You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low.
Guess again.
You have 8 attempts remaining to guess the number.
Make a guess: 47
You got it! The answer was 47
```

## What I Learned

- `check_answer()` has a silent bug worth knowing: when the guess is correct, it prints the win message but returns `None` — back in the `while` loop, `turns = None`, and the `if turns == 0` check never triggers (because `None != 0`), so it only works because the `while` condition `guess != answer` catches the exit. It works, but it's fragile — a cleaner version would `return turns` on the correct branch too
- Using constants for `EASY_LEVEL_TURNS` and `HARD_LEVEL_TURNS` means you change the difficulty in one place, not scattered across the code
- `set_difficulty()` silently defaults to hard for any input that isn't exactly `"easy"` — typos like `"Easy"` or `"EASY"` give the user hard mode without warning
- `from random import randint` vs `import random` — the first lets you call `randint()` directly; the second requires `random.randint()`. Neither is wrong, but `from x import y` is cleaner when you only need one thing from a module
- Structuring the game inside a `game()` function (rather than raw top-level code) makes it easy to add a "play again" loop later without restructuring anything
