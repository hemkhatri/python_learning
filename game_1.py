# import random

# user = int(input("1. Scissor\n2. Paper\n3. Rock\nChoose One : "))
# computer = random.randint(1, 3)

# print(f"Computer chose: {computer}")

# if user == computer:
#     print("It's a tie!")
# # Group all user-win scenarios
# elif (user == 1 and computer == 2) or \
#      (user == 2 and computer == 3) or \
#      (user == 3 and computer == 1):
#     print("You won!")
# else:
#     print("Computer won.")


# The "Higher or Lower" Number Guessing Game
# The computer picks a number between 1 and 100. You have to guess it, and the computer tells you if your guess is "Too High" or "Too Low."
# New Concept: Using a counter to tell the user how many tries it took them to win.
# Challenge: Limit the user to only 7 guesses. If they don't get it, they lose!

# import random
# number = random.randint(1, 100)
# n = 7
# while n > 0:
#     user_number = int(input(f"Guess the number ({n} times remaining) : "))
#     if(user_number > number):
#         print("Too High")
#     elif(user_number < number):
#         print("Too low")
#     else:
#         print(f"Correct! It's {number}")
#     n -= 1
# if(user_number != number):
#     print(f"You are unable to guess it. It was {number}")


# 2. Digital Dice Roller (The "Pig" Game)
# A 2-player game where you roll a 6-sided die.
# The Goal: Reach 50 points first.
# The Catch: If you roll a 1, you lose all the points you gathered in that specific turn. You have to decide when to "Hold" your points and pass the turn to the computer.
# New Concept: Nested while loops (one for the game, one for the player's turn).

# import random
# dicer = 6
# hold_roll = 2
# def get_random(options): #our dice
#     return random.randint(1, options)



# # print(dice)
# user = 0
# computer = 0
# total_point = 0
# current_point = 0

# def computer_asker():
#     global current_point
#     dice = get_random(hold_roll)
#     print(f"1. Hold\n2. Roll\nChoose One : {get_random(hold_roll)}")
#     options = dice
#     if options == 1 or options == 2:
#         if options == 1:
#             total_point += current_point
#             print(total_point)
#             user_turn()
#         else:
#             dice = get_random(dicer)
#             print(f"You got : {dice}")
#             if(dice != 1):
#                 current_point = current_point + dice
#             else:
#                 print(f"You lose total {current_point} points.")
#                 print(total_point)
#                 current_point = 0

# def user_asker():
#     global current_point
#     global total_point
#     options = int(input("1. Hold\n2. Roll\nChoose One : "))
#     if options == 1 or options == 2:
#         if options == 1:
#             total_point += current_point
#             print(total_point)
#             computer_turn()

#         else:
#             dice = get_random(dicer)
#             print(f"You got : {dice}")
#             if(dice != 1):
#                 current_point = current_point + dice
#             else:
#                 print(f"You lose total {current_point} points.")
#                 print(total_point)
#                 current_point = 0

# def computer_turn():
#     computer_asker()

# def user_turn():
#     user_asker()

# while True:
#     print(user_turn())
# # while True:
# #     options = int(input("1. Hold\n2. Roll\nChoose One : "))
# #     if options == 1 or options == 2:
# #         if options == 1:
# #             total_point += current_point
# #             print(total_point)
# #             computer_turn()
# #         else:
# #             dice = get_random()
# #             print(f"You got : {dice}")
# #             if(dice != 1):
# #                 current_point = current_point + dice
# #             else:
# #                 print(f"You lose total {current_point} points.")
# #                 print(total_point)
# #                 current_point = 0

import random

player_total = 0
comp_total = 0
target = 50

while player_total < target and comp_total < target:
    # --- PLAYER'S TURN ---
    current_turn_points = 0
    while True:
        print(f"\n--- YOUR TURN (Total Score: {player_total}) ---")
        choice = input("Press 'r' to Roll or 'h' to Hold: ").lower()
        
        if choice == 'r':
            die = random.randint(1, 6)
            print(f"You rolled a: {die}")
            if die == 1:
                print("Darn! You rolled a 1. Turn over, zero points earned.")
                current_turn_points = 0
                break
            else:
                current_turn_points += die
                print(f"Points this turn: {current_turn_points}")
        elif choice == 'h':
            player_total += current_turn_points
            break

    if player_total >= target: break

    # --- COMPUTER'S TURN ---
    current_turn_points = 0
    print(f"\n--- COMPUTER'S TURN (Total Score: {comp_total}) ---")
    while current_turn_points < 10: # Computer strategy: hold after 10 points
        die = random.randint(1, 6)
        print(f"Computer rolled: {die}")
        if die == 1:
            current_turn_points = 0
            break
        current_turn_points += die
    
    comp_total += current_turn_points
    print(f"Computer ends turn. New Total: {comp_total}")

print("\n--- GAME OVER ---")
if player_total >= target:
    print("You won!")
else:
    print("Computer won!")
