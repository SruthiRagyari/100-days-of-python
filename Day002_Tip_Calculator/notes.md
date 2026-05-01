# Day 2 - Tip Calculator

**What I Built**
A CLI tip calculator that takes a bill amount, tip percentage, and number of people, then splits the total evenly.

**Concepts Used**

- `float()` — convert input to a decimal number for money values
- `int()` — convert input to a whole number for tip % and people count
- Arithmetic operators — `+`, `/`, `*` to calculate the tip and split
- `:.2f` format specifier — round the output to 2 decimal places
- Variables — storing bill, tip, people, and intermediate calculations

**Code**

```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_multiplier = 1 + (tip / 100)
total_bill = (bill * tip_multiplier) / people

print(f"Each person should pay: ${total_bill:.2f}")
```

**Sample Output**

```
Welcome to the tip calculator!
What was the total bill? $150
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 3
Each person should pay: $56.00
```

**What I Learned**

- `input()` always returns a string — you must wrap it with `int()` or `float()` to do math
- `float` is used for money since bills can have decimals; `int` is enough for whole numbers
- Breaking the formula into two variables (`tip_multiplier`, `total_bill`) keeps the logic readable
- `:.2f` inside an f-string formats any float to exactly 2 decimal places, which is important for currency
