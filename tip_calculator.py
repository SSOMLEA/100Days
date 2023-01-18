# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


# Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
people = input("How many people to split the bill? ")
tip = input("What percentage tip would you like to give?: ")

def tip_calculator(total_bill, total_people, tip_pers):
    calculator_from_number_to_pers = int(tip_pers) / 100
    calculator_pers_from_total_bill = float(total_bill) * calculator_from_number_to_pers
    calculator_pers_per_person_plus_total_bill = calculator_pers_from_total_bill + float(total_bill)
    calculator_tip_per_friend = calculator_pers_per_person_plus_total_bill / int(total_people)
    final_result = round(calculator_tip_per_friend, 2)
    print(f"Each person should pay: ${final_result}")

tip_calculator(bill, people, tip)