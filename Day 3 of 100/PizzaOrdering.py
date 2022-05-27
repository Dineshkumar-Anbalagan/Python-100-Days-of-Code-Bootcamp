print("Welcome to Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")  #pizza size input: Small, Medium or Large
add_pepperoni = input("Do you want pepperoni? Y or N ") #pepperoni input : boolean Y or N
extra_cheese = input("Do you want extra cheese? Y or N ") #extra cheese input : boolean Y or N
total_bill = 0

'''
    Small Pizza: $15
    Medium Pizza: $20
    Large Pizza: $25

    Pepperoni for small pizza: +$2
    Pepperoni for medium and large pizza: +$3

    Extra cheese for any size pizza: +$1
'''

if size == "S":

    total_bill += 15

    if add_pepperoni == "Y":
        total_bill += 2
    if extra_cheese == "Y":
        total_bill += 1
    
    print(f"You total bill is ${total_bill}")

elif size == "M" or size == "L":
    if size == "M":
        total_bill += 20

    if size == "L":
        total_bill += 25
    
    if add_pepperoni == "Y":
        total_bill += 3
    
    if extra_cheese == "Y":
        total_bill += 1
    
    print(f"You total bill is ${total_bill}")

else:
    print("Please choose from any of the following sizes: S, M, or L ")

