#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show the their band name.

#5. Make sure the input cursor shows on a new line.


print("Welcome to brand name generator!!")
city_name = input("Enter the name of the city where you grew up in!?\n")
pet_name = input("Enter your pet name!?\n")
brand_name = city_name + " " + pet_name
print(f"Your brand name could be {brand_name}")