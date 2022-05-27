print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!! :) ")
    age = int(input("Enter your age? "))
    ticket_cost = 0
    if age < 12:
        print("Please pay $5")
        ticket_cost = 5
    elif age <= 18:
        print("Please pay $7")
        ticket_cost = 7
    else:
        print("Please pay $12")
        ticket_cost = 12
    
    wants_photo = input("Do you want a photo taken? Y/N ")
    
    if wants_photo == "Y":
        print("You've to pay 3 dollars extra")
        ticket_cost += 3
        print(f"Your final bill is {ticket_cost}")

    else:
        print(f"Your final bill is {ticket_cost}")

else:
    print("You cannot ride the rollercoaster! :(")