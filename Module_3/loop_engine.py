# items = ["apple", "banana", "cheese"]
# loop_item = iter(items)
# print(next(loop_item))
# print(next(loop_item))

#range
# for i, x in zip(range(1, 31), range(3, 31, 3)):
#     print(f"3 * {i} = {x}")
# else:
#     print("finished")

# for loop
# for x in range(5):
#     print(x)

# while loop
## Prints all letters except 'e' and 's'
# indexes = 0
# name = "Hello World"
# while indexes < len(name):
#     if name[indexes] == "e" or name[indexes] == " ":
#         indexes += 1
#         continue
#     print(name[indexes])
#     indexes += 1

# x  = 0
# while x < 10:
#     if x == 7:
#         x += 1
#         continue
#     print(x)
#     x += 1
# else:
#     print("No break")


# You have a list of item prices: [10.99, 5.50, 100.00, 25.00, 0.75]. Write a script that applies a 10% discount to every single item in that list and prints the new price.

# prices = [10.99, 5.50, 100.00, 25.00, 0.75]
# new_price = []
# for price in prices:
#     price = price - (0.1 * price)
#     new_price.append(price)
# print(new_price)

# # Write a script that asks a user to "Enter the secret password." If they get it wrong, the program should ask again... and again... and again. The program only stops and says "Access Granted" once they type the word Pythonistas.

# password = "Pythonistas"
# user_password = input("Enter the secret password : ")
# while(user_password != password):
#     # user_password
#     user_password = input("Enter the secret password : ")

# You are simulating a robot's battery. The battery starts at 100. Every time the robot "takes a step," the battery level drops by a random integer between 1 and 5. Write a script that continues taking steps and printing the current battery level until the battery hits 0 or lower.

import random
robo_battery = 100

while(robo_battery > 0):
    robo_battery = max(0, (robo_battery - random.randint(1, 5)))
    print(robo_battery)

# print(min(0, 4))