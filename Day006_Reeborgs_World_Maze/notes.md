# Day 6 - Reeborg's Maze Escape

## What I Built

A maze-solving algorithm for Reeborg's World that navigates any maze layout automatically using the right-hand wall-following rule.

## Concepts Used

- `def` — Define custom functions since Reeborg only has `turn_left()` built-in
- `turn_right()` — built by calling `turn_left()` three times
- `while` loop — keeps running until `at_goal()` is `True`
- Conditionals — `if / elif / else` to decide which direction to move
- Reeborg API — built-in functions like `front_is_clear()`, `right_is_clear()`, `at_goal()`, `move()`

## Code

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

# Right-hand rule maze solving algorithm
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

## Sample Output

Reeborg walks through the maze step by step and reaches the goal flag automatically — no matter which maze layout is loaded.

## Where to Run

This code does not run in a normal Python environment. It runs inside Reeborg's World, a browser-based robot simulator.

1. Go to 👉 [reeborg.ca/reeborg.html](https://reeborg.ca/reeborg.html)
2. Click **World** (top menu) → select **Maze**
3. Paste the code into the editor on the left
4. Click the **Run** button (▶) to watch Reeborg solve the maze

No installation needed — it runs entirely in your browser.

## What I Learned

- You can't always use built-in functions directly — sometimes you need to build your own (like `turn_right()`) by combining what's available
- The right-hand rule is a classic algorithm: always try to turn right first, move straight if you can't, and turn left only as a last resort
- `while not at_goal()` is a real-world example of looping until a condition is met, not just looping a fixed number of times
- Breaking logic into named functions makes the main loop clean and readable
