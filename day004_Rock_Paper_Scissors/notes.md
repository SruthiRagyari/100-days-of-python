# Day 4 - Rock Paper Scissors

## What I Built

A CLI Rock Paper Scissors game where the user picks Rock, Paper, or Scissors by entering a number, and the computer picks randomly. ASCII art displays both choices and the result is announced.

## Concepts Used

- `import random` — bring in Python's built-in random module
- `random.randint(0, 2)` — generate a random integer between 0 and 2 (inclusive) for the computer's choice
- Lists — storing the three ASCII art strings in `game_images` so they can be accessed by index
- List indexing — `game_images[user_choice]` to retrieve the matching art by position
- `int()` — convert the user's string input into an integer for comparison
- `if / elif / else` — chain multiple conditions to determine win, lose, or draw
- Input validation — checking if the number is out of range before deciding the result

## Code

```python
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
```

## Sample Output

```
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
0
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

You win!
```

## What I Learned

- Storing multi-line strings in a list is a clean way to map numbers to visual outputs — no need for a chain of `if` checks just to print the right image
- `random.randint(a, b)` includes both endpoints, so `randint(0, 2)` can return 0, 1, or 2
- Rock-Paper-Scissors logic can't be simplified to just "higher number wins" — Rock (0) beats Scissors (2) is the exception, so it needs its own explicit `elif`
- Input validation should be checked _after_ showing the user's choice art but _before_ the result logic — the current code handles this correctly with the ordering of `if` blocks
