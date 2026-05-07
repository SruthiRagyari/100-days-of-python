# Day 10 - Calculator

## What I Built

A CLI Calculator that performs add, subtract, multiply, and divide operations. After each calculation, the user can either continue chaining operations using the previous result, or start a fresh calculation from scratch.

## Concepts Used

- `import art` — import the art module for the logo display
- Functions as dictionary values — store `add`, `subtract`, `multiply`, `divide` as values in the `operations` dict so they can be called dynamically
- `operations[operation_symbol](num1, num2)` — look up a function by key and call it immediately in one line
- `float()` — accept decimal numbers as input, not just integers
- `for symbol in operations` — iterate over dictionary keys to print available operators
- Accumulator pattern — reassign `num1 = answer` to chain the result into the next operation
- Recursive `calculator()` call — start a completely fresh calculation by calling the function again instead of adding a nested loop
- Boolean flag (`should_accumulate`) — exit the current loop cleanly before the recursive call

## Code

```python
import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
```

## Sample Output

```
[Calculator ASCII logo]

What is the first number?: 10
+
-
*
/
Pick an operation: +
What is the next number?: 5
10.0 + 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: y

+
-
*
/
Pick an operation: *
What is the next number?: 3
15.0 * 3.0 = 45.0
Type 'y' to continue calculating with 45.0, or type 'n' to start a new calculation: n




[20 blank lines - screen cleared]




[Calculator ASCII logo]

What is the first number?:
```

## What I Learned

- Storing functions as dictionary values is a powerful pattern — instead of a long `if/elif` chain for each operator, you just do `operations[symbol](n1, n2)` and the right function runs automatically
- Functions in Python are first-class objects — you can put them in lists, dictionaries, or pass them as arguments just like any other value; `"+" : add` stores the function itself, not its result
- Using recursion to restart the calculator (`calculator()`) is elegant for a "start over" flow — it resets all local variables cleanly without needing a second outer loop
- The accumulator pattern (`num1 = answer`) is what makes chaining work — each loop iteration picks up exactly where the last one left off
- `float()` for input is a small but important choice — it handles `10.5 + 2.3` correctly where `int()` would crash on decimals
