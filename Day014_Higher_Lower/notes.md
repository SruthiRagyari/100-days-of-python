# Day 14 - Higher Lower Game

## What I Built

A CLI game where the user compares two Instagram-style accounts and guesses which has more followers. Correct guesses keep the streak alive and increment the score; one wrong answer ends the game and prints the final score. The winning account carries over as the next round's Account A, so the game chains continuously until the player loses.

## Concepts Used

- `random.choice(data)` — picks a random dictionary from a list; unlike `randint`, works directly on any sequence
- `format_data()` — a helper function that takes a dictionary and returns a formatted string; separates display logic from game logic
- `check_answer()` returns a boolean — cleaner than returning strings or numbers; the caller just checks `if is_correct`
- `account_b` initialized before the loop, then reassigned as `account_a` at the start of each iteration — this is the carry-over pattern that chains rounds without repeating the same account twice back-to-back
- `.lower()` on input — normalises `'A'` and `'a'` to the same value so the comparison doesn't break on capitalisation
- `game_should_continue = False` to exit the loop — instead of `break`, which is readable but slightly harder to trace in larger programs
- `print("\n" * 20)` — a simple screen-clear hack; not a real terminal clear but sufficient for a CLI game
- Top-level script structure (no wrapping `game()` function) — works here, but means adding a "play again" loop would require restructuring

## Code

```python
from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Takes a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
```

## Sample Output

```
[Logo]
Compare A: Instagram, a photo and video sharing social networking service, from United States.
[vs]
Against B: Cristiano Ronaldo, a Footballer, from Portugal.

Who has more followers? Type 'A' or 'B': b
[screen clear]
[Logo]
You're right! Current score: 1
Compare A: Cristiano Ronaldo, a Footballer, from Portugal.
[vs]
Against B: Ariana Grande, a Musician and actress, from United States.

Who has more followers? Type 'A' or 'B': a
[screen clear]
[Logo]
Sorry, that's wrong. Final score: 1.
```

## What I Learned

- The duplicate-account check (`if account_a == account_b`) is weak — it only re-draws once, so there's still a small chance of getting the same account again if the second draw also matches. A `while account_a == account_b` loop would actually fix it
- `check_answer()` returning a boolean is cleaner than Day 12's `check_answer()` which returned `turns` or `None` — booleans are unambiguous; the `None` bug from Day 12 can't happen here
- The carry-over pattern (`account_b` becomes next round's `account_a`) is efficient but easy to misread — it only works correctly because `account_b` is assigned _before_ the loop starts; if you moved that line inside the loop you'd break the chain
- `check_answer()` has a silent tie-handling issue: if both accounts have equal followers, the `else` branch fires and returns whether `user_guess == "b"` — meaning `"b"` is always "correct" on a tie, even though neither answer is actually right
- Unlike Day 12's `game()` wrapper, this code runs at the top level — noted in the Concepts section, this is the direct trade-off from that design choice
