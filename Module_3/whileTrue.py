# import socket

# def run_server():
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind(('localhost', 8080))
#     server.listen(1)
#     print("Server is listening...")
    
#     while True:
#         try:
#             client, addr = server.accept()
#             print(f"Connected to {addr}")
#             # Handle client...
#             client.close()
#         except KeyboardInterrupt:
#             print("Server shutting down")
#             break
#     server.close()

# run_server() # Uncomment to run




# The "Smart Thermostat" Polling Challenge
# Scenario: You are writing a script for a hardware thermostat. Instead of a list, you are monitoring a "live" temperature variable.
# The Setup:
# Initialize a variable current_temp = 20.
# Initialize a variable is_running = True.
# The Requirements:
# The Polling Loop: Create an infinite loop using while is_running:.
# State Update: Inside the loop, simulate the temperature rising by adding 2 to current_temp every iteration.
# The Skip (continue): If the temperature is exactly 24, the sensors are calibrating. Skip this iteration (don't print anything) and move to the next.
# The Placeholder (pass): If the temperature is 28, the "Cooling Fan" logic is not yet written. Use a placeholder so the code doesn't crash.
# The Boundary (break): If the temperature reaches or exceeds 34, the system is too hot. Print "Emergency Shutdown!" and break the loop.
# Normal Polling: For any other temperature, print: "Current Temperature: [temp]°C".
# Bonus: Use the for...else pattern's logic (or a while...else) to print "System cooled down successfully" if the loop were to exit normally (though in this specific logic, it will likely hit the break).

# https://share.google/aimode/gSL81u8O0S55BZbff
import time
current_temp = 20
is_running = True

while is_running:
    if current_temp == 24:
        current_temp += 2

        continue
    elif current_temp == 28:
        pass
    elif current_temp >= 34:
        time.sleep(1)
        print("Emergency Shutdown!")
        break
    else:
        print(f"Current Temperature : [{current_temp}]°C")
    
    current_temp += 2
    time.sleep(0.5)

print("\n")
print("Cooling Down Temperature....")
for temp in range(34, 20, -2):
    print(f"Current Temperature : [{temp}]°C")
    time.sleep(1)
else:
    print("System cooled down successfully!")