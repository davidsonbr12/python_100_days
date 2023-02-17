# A simple tip calculator.  Prints the total plus tip per person.

print("Welcome to the tip calculator.")
# Get total ticket price for the meal
while True:
    try:
        bill = float(input("What was the total bill? $"))
    except ValueError:
        print("You must enter a number")
        continue
    else:
        break

# Get tip % from predefined list of tips
while True:
    tip_amount = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    if tip_amount not in (10, 12, 15):
        print("Please select from the provided tip options.")
    else:
        break

# Get size of party
while True:
    party_size = int(input("How many people to split the bill? "))
    if party_size < 1:
        print("Party size must be 1 or more.")
    else:
        break

# Calculations to settle the final bill per person
tip_percent = tip_amount / 100
total_tip_amount = bill * tip_percent
total_bill_amount = bill + total_tip_amount
total_per_person = round(total_bill_amount / party_size, 2)
final_bill = "{:.2f}".format(total_per_person)

print(f"Each person should pay: ${final_bill}")
