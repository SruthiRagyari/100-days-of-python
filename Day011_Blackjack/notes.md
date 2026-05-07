# Day 11 - Blackjack

## What I Built

A CLI Blackjack game played against the computer. The player draws cards trying to reach 21 without going over, while the computer automatically draws until it hits 17 or above. Handles Blackjack (21 in 2 cards), Ace value adjustment, and all win/lose/draw conditions.

## Concepts Used

- `random.choice(cards)` — draw a random card from the deck on each call
- Multiple functions with single responsibilities — `deal_card()`, `calculate_score()`, `compare()`, and `play_game()` each do exactly one job
- `sum(cards)` — calculate the total hand value from a list of integers
- Ace adjustment logic — if 11 is in the hand and total exceeds 21, remove 11 and append 1 to fix the bust
- Returning `0` as a special score — represents Blackjack (21 in exactly 2 cards), used as a sentinel value throughout
- `for _ in range(2)` — deal exactly 2 cards each to player and computer at the start; `_` signals the loop variable is intentionally unused
- Two separate `while` loops — one for the player's turn (interactive), one for the computer's turn (automatic)
- `compare(u_score, c_score)` — centralises all win/lose/draw logic in one place with ordered conditions

## Code

```python
import random
from art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
```

## Sample Output

```
Do you want to play a game of Blackjack? Type 'y' or 'n': y




[20 blank lines - screen cleared]




[Blackjack ASCII logo]

Your cards: [10, 6], current score: 16
Computer's first card: 8
Type 'y' to get another card, type 'n' to pass: y
Your cards: [10, 6, 4], current score: 20
Computer's first card: 8
Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 6, 4], final score: 20
Computer's final hand: [8, 5, 7], final score: 20
Draw 🙃

Do you want to play a game of Blackjack? Type 'y' or 'n': y




[20 blank lines - screen cleared]




[Blackjack ASCII logo]

Your cards: [11, 10], current score: 0
Computer's first card: 6

Your final hand: [11, 10], final score: 0
Computer's final hand: [6, 9, 4], final score: 19
Win with a Blackjack 😎

Do you want to play a game of Blackjack? Type 'y' or 'n': n
```

## What I Learned

- Using `0` as a sentinel value for Blackjack is a clever design choice — it lets `compare()` handle the Blackjack condition with a simple equality check rather than passing around a separate boolean flag
- The Ace adjustment (`remove(11), append(1)`) only handles one Ace busting at a time, which is fine here since a hand can only have one active Ace worth 11 before going over 21
- `for _ in range(2)` is the Pythonic way to repeat something a fixed number of times when you don't need the loop index — `_` is a convention that signals "I'm intentionally ignoring this variable"
- Keeping the computer's second card hidden (`computer_cards[0]` only) during the player's turn is authentic Blackjack rules enforced through a simple index choice, not any extra logic
- The order of conditions in `compare()` matters — checking `c_score == 0` before `u_score > 21` ensures the computer's Blackjack is announced correctly even if the player also busted
