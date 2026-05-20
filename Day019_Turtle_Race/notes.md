# Day 19 - Turtle Race

## What I Built

A turtle graphics race where 6 colored turtles move across the screen in random increments. Before the race starts, the user bets on a color via a pop-up input box, and the program announces whether they won or lost once a turtle crosses the finish line.

## Concepts Used

- `Screen().setup(width, height)` — sets the window dimensions before anything is drawn
- `screen.textinput()` — opens a GUI dialog box and returns the user's input as a string; returns `None` if cancelled
- **Parallel lists** — `colors` and `y_positions` share the same index so `colors[i]` and `y_positions[i]` always belong to the same turtle
- `turtle.goto(x, y)` — moves turtle to an absolute coordinate without drawing
- `turtle.xcor()` — returns the turtle's current x position; used to detect when it crosses the finish line
- `turtle.pencolor()` — returns the turtle's color as a string; used to identify the winner
- `random.randint(0, 10)` — each turtle moves a different random distance per loop iteration, making the race unpredictable
- `if user_bet:` — guards against `None` (user closed the dialog without input) so the race only starts with a valid bet

## Code

```python
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
```

## Sample Output

```
# Dialog box appears:
# "Which turtle will win the race? Enter a color: " → user types "blue"

# Race runs visually in the turtle window, then in terminal:
You've lost! The red turtle is the winner!
```

## What I Learned

- `turtle.xcor() > 230` uses 230 instead of 250 (half the 500px window width) to account for the turtle shape's own size — crossing at 250 would mean the turtle visually exits the screen before the win triggers
- The `while` loop iterates over all 6 turtles on every tick — once a winner is found, `is_race_on = False`, but the `for` loop still finishes its current iteration, meaning turtles after the winner in the list still call `turtle.forward()` one more time. It doesn't affect correctness here but is worth knowing
- `random.randint(0, 10)` includes 0, so a turtle can stay still on any given tick — this makes the race feel more realistic with natural stalls and surges rather than steady uniform movement
- `turtle.pencolor()` is used to retrieve the winning color instead of tracking an index — this works because `.color()` sets both fill and pen color together, so `.pencolor()` reliably returns the string that was passed to `.color()` at setup
- `if user_bet:` is a clean `None` guard — `screen.textinput()` returns `None` if the dialog is dismissed, and an empty string `""` if submitted blank; both are falsy, so neither starts the race, which is the correct behavior
