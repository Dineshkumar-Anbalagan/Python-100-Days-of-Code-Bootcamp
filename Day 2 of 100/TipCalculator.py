print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? ")[1:])
tip_percentage = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))
print(f"Each person should pay ${(total_bill + (total_bill*(tip_percentage/100)))/no_of_people}")
