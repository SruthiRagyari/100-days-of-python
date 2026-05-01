# Day 1 - Band Name Generator

## What I Built

A simple CLI program that generates a band name by combining your childhood city and pet name.

## Concepts Used

- `print()` — display output to the user
- `input()` — take user input and store it in a variable
- f-string — embed variables inside a string using `f"...{variable}..."`
- Variables — storing user input in `city` and `pet_name`

## Code

```python
print("Welcome to Band Name Generator...")
city = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
print(f"Your Band Name could be {city} {pet_name}.")
```

## Sample Output

```
Welcome to Band Name Generator...
What's the name of the city you grew up in?
Nellore
What's your pet's name?
Bruno
Your Band Name could be Nellore Bruno.
```

## What I Learned

- Python runs line by line from top to bottom
- `input()` always returns a string
- f-strings are the cleanest way to mix variables into text
- `\n` inside a string moves the cursor to a new line
