# Day 16 - Coffee Machine (OOP)

## What I Built

A CLI coffee machine simulation refactored into four files using Object-Oriented Programming. Three classes — `Menu`, `CoffeeMaker`, and `MoneyMachine` — each handle one responsibility, and `main.py` wires them together into a running loop.

## Project Structure

```
day-16/
├── main.py
├── menu.py
├── coffee_maker.py
└── money_machine.py
```

## Concepts Used

- **Classes and objects** — `Menu`, `CoffeeMaker`, and `MoneyMachine` are each instantiated once in `main.py` and used throughout the loop
- **`__init__`** — sets up starting state (resources, profit, menu items) when each object is created
- **Instance attributes** — `self.resources`, `self.profit`, `self.menu` store state that persists and changes across method calls
- **Class attributes** — `CURRENCY` and `COIN_VALUES` in `MoneyMachine` are shared across all instances and written in ALL_CAPS by convention
- **Methods with return values** — `is_resource_sufficient()` returns `True/False`; `make_payment()` returns `True/False`; both are used together in one `if` condition in `main.py`
- **Short-circuit evaluation** — `if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost)` — if resources are insufficient, `make_payment()` is never called at all
- **Separation of concerns** — each class owns exactly one domain: menu data, physical resources, and money handling
- **Multi-file imports** — `from menu import Menu` pulls a specific class from another file in the same directory

## Code

### main.py

```python
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"what would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
```

### menu.py

```python
class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
```

### coffee_maker.py

```python
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
```

### money_machine.py

```python
class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
```

## Sample Output

```
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0

what would you like? (latte/espresso/cappuccino/): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!

what would you like? (latte/espresso/cappuccino/): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

what would you like? (latte/espresso/cappuccino/): off
```

## What I Learned

- Splitting code across files forces you to think clearly about what each piece _owns_ — `CoffeeMaker` never touches money, `MoneyMachine` never touches ingredients; that boundary makes both easier to debug and change independently
- Class attributes (`CURRENCY`, `COIN_VALUES`) vs instance attributes (`self.profit`) — class attributes are defined outside `__init__` and shared by all instances; instance attributes are set inside `__init__` and unique to each object
- `make_payment()` has a state bug worth noting: `self.money_received` is reset to `0` at the end of each call, but it's _accumulated_ inside `process_coins()` using `+=` — if `process_coins()` were ever called twice in one transaction, it would add to leftover state. It works here because the flow is linear, but it's fragile
- Short-circuit `and` in `main.py` means if `is_resource_sufficient()` returns `False`, the user is never asked to insert coins — the order of the two conditions in that `if` statement actually matters for UX
- `find_drink()` returns `None` silently if the drink isn't found, and `main.py` passes that `None` directly into `is_resource_sufficient()` — which would crash with an `AttributeError`. The `print("Sorry...")` in `find_drink` doesn't stop execution, so this is a real unhandled edge case in the code
