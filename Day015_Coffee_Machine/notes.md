# Day 15 - Coffee Machine

## What I Built

A CLI coffee machine simulator that takes drink orders (espresso, latte, cappuccino), checks if ingredients are available, processes coin-based payments, dispenses the drink, and tracks profit. Typing `report` prints current resource levels and earnings; typing `off` shuts the machine down.

## Concepts Used

- `global profit` — explicitly declares that `profit` inside the function refers to the module-level variable, not a new local one; required when you want to _modify_ a global from inside a function (reading it doesn't need `global`)
- Nested dictionaries (`MENU`) — each key maps to another dictionary; accessed with chained keys like `MENU["latte"]["cost"]`
- `for item in order_ingredients` — iterates over dictionary keys; `order_ingredients[item]` gives the value for each key
- Boolean-returning functions (`is_resource_sufficient`, `is_transaction_successful`) — each function handles its own print feedback and returns `True`/`False`; the main loop just checks the result
- `round(value, 2)` — limits floating point results to 2 decimal places; important here because coin math like `0.1 + 0.05` produces floating point noise without it
- Guard-clause chaining — `if is_resource_sufficient(...):` wraps `if is_transaction_successful(...):` which wraps `make_coffee()` — each layer only runs if the previous passed
- `is_on = True` / `is_on = False` loop control — cleaner than `break` for a machine that has a named on/off state

## Code

```python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
```

## Sample Output

```
What would you like? (espresso/latte/cappuccino): report
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0

What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
how many quarters?: 10
how many dimes?: 0
how many nickles?: 0
how many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!

What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

What would you like? (espresso/latte/cappuccino): off
```

## What I Learned

- `global profit` is a code smell worth knowing — it works, but it means `is_transaction_successful` is secretly modifying state outside its scope. A cleaner design would return the drink cost and let the caller update `profit`, keeping the function pure
- The `else` branch for invalid drink names (anything that isn't `off`, `report`, or a valid menu item) will crash with a `KeyError` on `MENU[choice]` — there's no input validation; typing `"tea"` breaks the program
- `is_resource_sufficient` stops and returns `False` on the _first_ insufficient ingredient — so if both water and coffee are low, the user only hears about water. A version that collects all shortages before returning would give better feedback
- Coin math in floats is inherently imprecise — `round()` patches the display but doesn't fix the underlying representation. For real money handling you'd use Python's `decimal` module
- The duplicate-account-style bug from Day 14 has an equivalent here: resources are never restocked, so the machine will eventually refuse all orders silently — there's no "restock" command
- Top-level loop (no `main()` wrapper) — same trade-off as Day 14; noted here because Day 15 is where this pattern starts to matter more as the program gets larger
