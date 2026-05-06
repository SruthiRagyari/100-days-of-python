# Day 9 - Secret Auction

## What I Built

A CLI Secret Auction program where multiple bidders enter their name and bid amount privately. After all bids are collected, it finds and announces the highest bidder as the winner.

## Concepts Used

- `from art import logo` — import only a specific item from a module
- Dictionary (`{}`) — store each bidder's name as the key and their bid amount as the value
- `for bidder in bidding_record` — iterate over dictionary keys
- `bidding_record[bidder]` — access a dictionary value using its key
- Function with a parameter — pass the entire `bids` dictionary into `find_highest_bidder()`
- Comparison inside a loop — track the running highest bid and update the winner whenever a larger one is found
- `print("\n" * 20)` — simulate screen clearing so the next bidder can't see previous bids
- Boolean flag (`continue_bidding`) — control the auction loop until no more bidders remain

## Code

```python
from art import logo
print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
```

## Sample Output

```
[Secret Auction ASCII logo]

What is your name?: Sruthi
What is your bid?: $500
Are there any other bidders? Type 'yes' or 'no'.
yes




[20 blank lines - screen cleared]




What is your name?: Ravi
What is your bid?: $850
Are there any other bidders? Type 'yes' or 'no'.
yes




[20 blank lines - screen cleared]




What is your name?: Priya
What is your bid?: $720
Are there any other bidders? Type 'yes' or 'no'.
no
The winner is Ravi with a bid of $850
```

## What I Learned

- A dictionary is the natural data structure for this problem — names and bids are a key-value pair by nature, and looking up any bidder's amount is instant
- `for bidder in bidding_record` iterates over keys, not values — you then use `bidding_record[bidder]` to get the value, which is worth remembering as a pattern for scanning dictionaries
- `print("\n" * 20)` is a simple but effective privacy trick — it pushes previous output off the screen without needing any OS-specific clear command
- Starting `highest_bid = 0` and `winner = ""` before the loop is the standard pattern for tracking a running maximum — the first bid will always beat 0, so the variables get set correctly from the first iteration
- `from art import logo` vs `import art` — importing only what you need is cleaner and means you write `logo` directly instead of `art.logo` everywhere
