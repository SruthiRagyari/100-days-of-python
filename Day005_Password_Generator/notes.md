# Day 5 - Password Generator

## What I Built

A CLI password generator that asks how many letters, symbols, and numbers you want, then builds a randomized password by sampling from character sets and shuffling the result.

## Concepts Used

- `import random` — access Python's random module for sampling and shuffling
- `random.choices(list, k=n)` — pick `n` random items from a list _with_ replacement
- `random.shuffle(list)` — shuffle a list **in place** to mix the character order
- List concatenation — combining three separate `random.choices()` results with `+` into one list
- `"".join(list)` — collapse a list of characters into a single string
- `int()` — convert user input strings to integers for the `k=` parameter

## Code

```python
import random

# Character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# User input
nr_letters = int(input("How many letters would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Generate password parts
password_list = (
    random.choices(letters, k=nr_letters) +
    random.choices(symbols, k=nr_symbols) +
    random.choices(numbers, k=nr_numbers)
)

# Shuffle to make it random order
random.shuffle(password_list)

# Convert list to string
password = "".join(password_list)

# Output
print(f"Your password is: {password}")
```

## Sample Output

```
Welcome to the PyPassword Generator!
How many letters would you like?
6
How many symbols would you like?
2
How many numbers would you like?
3
Your password is: k#3Bx&m7Qp2
```

## What I Learned

- `random.choices()` samples _with_ replacement (same character can appear twice), which is fine for passwords — `random.sample()` would prevent repeats but limits length to the list size
- Generating each character type separately first _guarantees_ the counts the user asked for — if you just picked randomly from one big combined list you couldn't control the mix
- `random.shuffle()` modifies the list directly and returns `None`, so you shuffle first, _then_ call `"".join()` — not the other way around
- `"".join(list)` is the standard Python way to turn a character list into a string; the `""` means no separator between characters
