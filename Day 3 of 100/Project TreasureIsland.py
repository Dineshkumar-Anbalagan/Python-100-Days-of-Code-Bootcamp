print("Welcome to Treasure Island")
print("Your Mission is to find the lost treasure")

direction1 = input('You\'re at a cross road. where do you want to go? Type "left" or "right" ')
if direction1 == "left":
    direction_2 = input("You came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ")
    if direction_2 == "wait":
        color = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        if color == "yellow":
            print("You Win!!")
        else:
            print("Game Over.")
    else:
        print("You got attacked by a angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
