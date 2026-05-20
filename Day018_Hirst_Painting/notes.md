# Day 18 - Hirst Painting

## What I Built

A turtle graphics program that recreates Damien Hirst's spot paintings — a 10×10 grid of colored dots drawn using a curated palette of RGB tuples extracted from an actual Hirst painting.

## Concepts Used

- `turtle_module.colormode(255)` — switches turtle from default 0–1 float color mode to 0–255 RGB integers so the color tuples work directly
- `tim.penup()` — lifts the pen so turtle moves without drawing lines between dots
- `tim.hideturtle()` — hides the arrow cursor so only the dots are visible
- `tim.dot(size, color)` — draws a filled circle of given diameter at the current position
- `random.choice(list)` — picks a random RGB tuple from the color list each time
- `dot_count % 10 == 0` — modulo check to detect the end of each row of 10 dots
- `tim.setheading(angle)` — sets absolute direction: `0` = right, `90` = up, `180` = left, `225` = diagonal down-left
- `tim.forward(300)` with heading `225` — moves diagonally to position the starting dot at the bottom-left before the grid begins
- `screen.exitonclick()` — keeps the window open until clicked

## Code

```python
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
              (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
              (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77),
              (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
              (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
              (107, 127, 153), (174, 94, 97), (176, 192, 209)]

# Move to bottom-left starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
```

## Sample Output

A 10×10 grid of 20px colored dots spaced 50px apart, each a random color from the palette, centered in the turtle window.

## What I Learned

- `colormode(255)` has to be called before any color is set — if you pass RGB tuples without it, turtle throws a error because it expects floats between 0 and 1 by default
- The `setheading(225)` + `forward(300)` trick at the start is pure geometry — 225° is exactly down-left at 45°, which shifts the turtle away from center so the finished grid appears visually centered in the window rather than drawn from the middle outward
- `dot_count % 10 == 0` catches dot 10, 20, 30... — the row-end logic runs _after_ the last dot of each row is drawn and the turtle has already moved forward one step, so the carriage-return sequence (up 50, left 500, reset heading) lands it correctly at the start of the next row
- `tim.forward(500)` goes left by exactly 10 × 50px to return to the left edge — this number is hardcoded to match the 10-dot row width, so if you changed `number_of_dots` to draw more columns, this line would also need updating
- The color list was extracted from a real Hirst painting using the `colorgram` library (covered earlier in Day 18) — the palette isn't random invention, it's sampled pixel data, which is why the colors feel cohesive rather than garish
