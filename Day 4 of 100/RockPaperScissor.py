import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor : "))

'''

International Rock Paper Scissor Rules:

    1. Rock wins against scissors.

    2. Scissors win against paper.

    3. Papers wins againt rock.

'''

def s1(player_choice):

    import random

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    options = [rock, paper, scissors]

    computer_choice = options[random.randint(0,2)]

    print("computer choice : ", computer_choice)

    player_choice = options[player_choice]

    print("player choice : ", player_choice)

    if (
            (player_choice == rock and computer_choice == scissors) or 
            (player_choice == scissors and computer_choice == paper) or 
            (player_choice == paper and computer_choice == rock)
        ):
        
        print("player wins")

    elif (
            (computer_choice == rock and player_choice == scissors) or 
            (computer_choice == scissors and player_choice == paper) or 
            (computer_choice == paper and player_choice == rock)
        ):

        print("computer wins")
    
    elif computer_choice == player_choice:

        print("Match Draw!")


s1(player_choice)
