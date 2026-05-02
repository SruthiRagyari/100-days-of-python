# Day 3 - Treasure Island 🏝️

## What I Built

A text-based adventure game where the player makes choices to find the treasure. Wrong choices end the game; only the right path leads to victory.

## Concepts Used

- `print()` — display story text and outcomes to the user
- `input()` — take player choices and store them in variables
- `.lower()` — convert input to lowercase so "Left" and "left" are treated the same
- `if / elif / else` — conditional logic to branch the story based on player choices
- **Nested `if` statements** — placing one `if` block inside another to handle multi-step decisions
- `r''' ... '''` — raw multi-line string used to print ASCII art without escape issues

## Code

```python
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Left or Right? ").lower()

if choice1 == "left":

    choice2 = input("Swim or Wait? ").lower()

    if choice2 == "wait":

        choice3 = input("Which door? Red, Blue, or Yellow? ").lower()

        if choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        elif choice3 == "yellow":
            print("You Win!")
        else:
            print("Game Over.")

    else:
        print("Attacked by trout. Game Over.")

else:
    print("Fall into a hole. Game Over.")
```

## Sample Output

```
Welcome to Treasure Island.
Your mission is to find the treasure.
Left or Right? left
Swim or Wait? wait
Which door? Red, Blue, or Yellow? yellow
You Win!
```

## What I Learned

- `.lower()` makes input case-insensitive — the player can type "Left", "LEFT", or "left" and it all works the same
- **Nested `if` statements** let you build a decision tree — each level of indentation is a new branch
- `elif` is used when you have more than two possible outcomes for the same input
- The `else` at the end of an `if/elif` chain catches any unexpected input as a fallback
- Python uses **indentation** (not curly braces) to define which code belongs inside which `if` block — getting this wrong breaks the logic
- `r''' ... '''` is a raw string — the `r` prefix tells Python to ignore backslashes, which is useful for ASCII art that has special characters
