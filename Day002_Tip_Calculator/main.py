print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_multiplier = 1 + (tip / 100)
total_bill = (bill * tip_multiplier) / people

print(f"Each person should pay: ${total_bill:.2f}")
