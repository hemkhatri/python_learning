

# total_size = 500
# minutes = 60
# hour, minutes = divmod(total_size, minutes)
# print(hour, minutes)

# current_position = 9
# moment = 4
# total_grid = 10

# print((current_position + moment) % total_grid)

# owned = 97
# big_box = 25
# quarters, pennies = divmod(owned, big_box) 
# print(f"Quarters: {quarters}, Pennies: {pennies}")

# You are a developer for a shipping company. You have 1,245 identical items that need to be packed and shipped.
# Each Standard Shipping Crate can hold exactly 12 items.
# Any items that don't fill a whole crate are put into a "Single Item" envelope.
# Your Task:
# Using the "System Layer" math (// and %), calculate:
# How many Full Crates will you ship?

# identical = 1245
# standard_shipping = 12
# full, single = divmod(identical, standard_shipping)
# print(full, single)



# You are building a payroll system. An employee works in 8-hour shifts. If they work more than 8 hours, the extra time is considered Overtime.
# The Scenario:
# An employee worked a total of 51 hours this week.
# The Rules:
# Calculate how many Full Shifts (8 hours each) they worked.
# Calculate the Extra Hours (the remainder).
# The Logic Twist: The company only pays an "Overtime Bonus" if the Extra Hours are greater than 5.
# Your Task:
# Find the full_shifts and extra_hours using your math tools.
# Write a Boolean (Identity/Equality) check to see if they get the bonus.
# What are the numbers, and do they get the bonus (True or False)?


# total_hours = 55
# standard_shift = 8

# full_shift, overtime = divmod(total_hours, standard_shift)

# # full_shift = 51 // 8
# # ot = 55 % 8

# print(full_shift)
# print(overtime)

# print(overtime > 5)
# # print(standard)
# # print(overtime)




# You are building a trading app. A user wants to buy as many shares of Apple (AAPL) as possible with their cash.
# The Data:
# User's Cash: $1,040
# Share Price: $150 per share.
# The Task:
# total_shares: Use // to find how many full shares they can buy.
# leftover_cash: Use % to find the money remaining in their wallet.
# The "Safety" Logic: The app has a rule: A user can only trade if they can buy at least 5 shares AND have less than $200 leftover.
# Your Code Goal:
# Calculate the total_shares and leftover_cash. Then, write a Boolean check using and (Phase 1) to see if they are allowed to trade.
# Will the result be True or False?
# (Think carefully about the Short-Circuiting we learned in Phase 1!)

# user_cash = 1040
# share_price = 150

# user_can_buy, left_over = divmod(user_cash, share_price)

# if user_can_buy >= 5 and left_over < 200:
#     print("Allowed to trade")
# else:
#     print("Not allowed to trade")



# READ = 1
# WRITE = 2

# user_perm = 0

# # Use | to add READ
# user_perm = user_perm | READ

# # Now use | to add WRITE to the same user
# user_perm = user_perm | WRITE

# print(user_perm) # What is the final number?


# view = 1
# edit = 2
# delete = 4
# share = 8
# copy = 16

# user_permission = 0 #default

# user_permission = view | edit
# print(user_permission)


# user_permission = user_permission | copy

# print(user_permission)
# if(user_permission & delete):
#     print("access")
# else:
#     print("denied")

# user_permission = user_permission & ~delete

# print(user_permission)




# The "Security Camera" System 📹
# You are coding a security system with 4 levels of access.
# Define the Flags (Use the << shift trick to create these values):
# MOTION_SENSE (Shift 0)
# RECORD (Shift 1)
# NIGHT_VISION (Shift 2)
# ALARM (Shift 3)
# The Setup:
# Create a variable camera_settings starting at 0.
# Add MOTION_SENSE and ALARM to the settings.
# Add NIGHT_VISION to the settings.
# The Logic:
# The camera triggers a "Full Alert" ONLY if it has both ALARM and RECORD permissions.
# Your Task:
# What is the current value of camera_settings?
# Write the Boolean check (using &) to see if "Full Alert" is triggered.
# Does the system trigger the alert? (True or False?)
# Show me the code and the final results. No hints.


# MOTION_SENSE = 1 << 0
# RECORD = 1 << 1
# NIGHT_VISION = 1 << 2
# ALARM = 1 << 3

# camera_settings = 0
# camera_settings = MOTION_SENSE | ALARM 
# camera_settings = camera_settings | NIGHT_VISION

# if (camera_settings & ALARM) and (camera_settings & RECORD):
#     print("Full Alert")

# print(bool(camera_settings & ALARM) and (camera_settings & RECORD))

# print(camera_settings)



# You are building a Game Character Controller.
# Define these 4 Flags (using <<):
# CAN_JUMP (Shift 0)
# CAN_FLY (Shift 1)
# IS_INVINCIBLE (Shift 2)
# HAS_WEAPON (Shift 3)
# The Scenario:
# A player picks up a "Power Up". Use | to give them CAN_JUMP and CAN_FLY.
# The player picks up a "Shield". Use | to give them IS_INVINCIBLE.
# The Glitch: A monster hits the player! Use ^ (XOR) to Toggle their IS_INVINCIBLE status (it was ON, now it should be OFF).
# The Test:
# Calculate the final player_state value.
# Write a Single Line check to see if the player CAN_FLY but NOT jump.
# Can you write the code and tell me the final player_state number?


# CAN_JUMP = 1 << 0
# CAN_FLY = 1 << 1
# IS_INVINCIBLE = 1 << 2
# HAS_WEAPON = 1 << 3

# POWER_UP = CAN_JUMP | CAN_FLY
# SHIELD = IS_INVINCIBLE
# player_state = 0
# player_state = POWER_UP | SHIELD

# #monster hits
# player_state = player_state ^ IS_INVINCIBLE

# print(player_state)

# # Check if Fly is ON (&) AND Jump is OFF (& ~)
# print(bool(player_state & CAN_FLY) and not bool(player_state & CAN_JUMP))
# # Take the 8 (1000) and move it right 3 spots
# print(HAS_WEAPON >> 3) # Result: 1 (The switch is ON!)


# READ = 0b0001  # Binary for 1
# WRITE = 0b0010 # Binary for 2

# # ADD: User gets Read AND Write
# user_perms = READ | WRITE  # Result: 0b0011 (3)

# # CHECK: Does the user have Write?
# if user_perms & WRITE:
#     print("Access Granted")




# Exercise 1: The "Safety Net" (Short-Circuiting)
# You are writing a function to check if a user is "VIP." To be a VIP, they must exist in the database and have a score over 100.
# The Setup:
# python
# user_data = None  # Imagine the database returned nothing
# Use code with caution.

# The Goal: Write a single if statement that checks if user_data is not None AND if user_data["score"] > 100.
# Constraint: Your code must not crash (raise a TypeError) even though user_data is None.

# user_data = None  # Imagine the database returned nothing
# # user_data= {
# #     "score" : 23,
# #     "name" : "Hem"
# # }
# try:
#     print(user_data != None and user_data["score"] > 100)
#     print(user_data["score"])
# except TypeError as e:
#     print("Error : ", e)
    




# You have 500 minutes.
# Use // to find out how many full hours are in 500 minutes.
# Use % to find out how many leftover minutes remain.
# What are the two numbers?

# total_mins = 500
# minutes, seconds = divmod(total_mins, 60)
# print(minutes, seconds)



# READ = 1 << 0
# WRITE = 1 << 1
# EXECUTE = 1 << 2

# user_per = 0
# user_per = READ | WRITE
# print(user_per)
# print(bool(user_per & WRITE))
# user_per = user_per ^ READ
# print(user_per)




# The Scenario: High-Security Hub
# You are building the core logic for a Security Hub Controller that manages a secure server room. To pass the system's certification, your code must handle the following three requirements efficiently:
# 1. The Sensor Rotation (Phase 2)
# The room has exactly 8 environment sensors (indexed 0 through 7). The hub runs a continuous monitoring loop. Every time the scan_next() function is called, the system must increment the current_sensor_index.
# Task: If the current index is 7, the next call must automatically reset the index to 0 without using an if-else statement.
# 2. The Safety Guard (Phase 1)
# The controller receives a sensor_data object from the hardware. However, if a sensor is physically unplugged, the hardware returns None. If it is plugged in, it returns an object with a .value attribute (an integer).
# Task: Write a single-line Boolean expression that evaluates to True ONLY if the sensor_data is NOT None AND the .value is greater than 100. The expression must be "crash-proof" (it must not raise an error if sensor_data is None).
# 3. The Room State (Phase 3)
# The room’s security status is stored in a single integer called system_state.
# Bit 0 (Value 1): Motion Detected
# Bit 1 (Value 2): Door Unlocked
# Bit 2 (Value 4): Alarm Triggered
# Task: You need to perform two specific bitwise actions:
# Create an expression to force-enable the "Alarm Triggered" bit without changing any other bits.
# Create an expression to check if "Motion Detected" is currently active (returning a non-zero value if it is).


# current_index = 0
# def scan_next():
#     global current_index
#     print(current_index)
#     current_index = (current_index + 1) % 8

# # while True:
# #     scan_next()
# sensor_data = [1, 0, 1, 0, 1]
# for data in sensor_data:
#     if data == False:
#         data = None
#     print(bool(data))

# --- INITIAL STATE ---
current_sensor_index = 0
system_state = 0  # Starts with no flags set (Binary: 000)

# Requirement 1: The Sensor Rotation (Phase 2)
# Increments 0-7 then resets to 0 automatically
def scan_next():
    global current_sensor_index
    current_sensor_index = (current_sensor_index + 1) % 8
    return current_sensor_index

# Requirement 2: The Safety Guard (Phase 1)
# Uses short-circuiting to check the attribute safely
def check_safety(sensor_data):
    # If sensor_data is None, the 'and' stops and returns False
    # This prevents the 'AttributeError' on sensor_data.value
    if sensor_data is not None and sensor_data.value > 100:
        return "CRITICAL: High Reading Detected"
    return "Status: Normal or Sensor Offline"

# Requirement 3: The Room State (Phase 3)
def update_system_status():
    global system_state
    
    # Task A: Force-enable the "Alarm Triggered" bit (Value 4)
    # The '|' operator turns the bit ON without changing others
    system_state |= 4 
    
    # Task B: Check if "Motion Detected" is active (Value 1)
    # The '&' operator masks the number to look ONLY at bit 0
    motion_active = (system_state & 1) != 0
    
    return motion_active

# --- TEST CASE ---
class Sensor:
    def __init__(self, val):
        self.value = val

# Simulation: Sensor index rotates, and we check a 'None' sensor
print(f"Next Sensor Index: {scan_next()}")  # Returns 1
print(check_safety(None))                   # Returns "Status: Normal..." (No crash!)
print(f"Motion Active: {update_system_status()}") # Checks bit 0
