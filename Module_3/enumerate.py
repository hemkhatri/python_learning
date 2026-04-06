# import json
# logs = ["User logged in", "Connection Lost", "Database updated"]
# for index, log in enumerate(logs, start = 1):
#     print(f"Log {index} : {log}")

# # #indexed list
# indexed_list = dict(enumerate(logs))
# print(type(indexed_list))
# print(json.dumps(indexed_list, indent=4))

# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)
# print(next(y))
# print(next(y))
# print(next(y))
# # print(next(y))


# The Mission
# Write a script that loops through the transmission list and prints a report.
# Your constraints:
# Use enumerate() to assign a Packet ID to each string, starting at 100.
# If a string contains the word "ERROR", print: [ALARM] Packet #[ID]: [Content].
# If the packet is clean, print: [OK] Packet #[ID]: Decrypted.
# Bonus: If the Packet ID is an even number AND contains an error, flag it as [CRITICAL].
# The Data:
# python
# transmission = [
#     "Sensor sync complete",
#     "ERROR: Oxygen levels low",
#     "Coordinates received",
#     "ERROR: Navigation thruster offline",
#     "Communication link stable"
# ]

transmission = [
    "Sensor sync complete",
    "ERROR: Oxygen levels low",
    "ERROR: Oxygen levels low",
    "Coordinates received",
    "ERROR: Navigation thruster offline",
    "Communication link stable"
]
for ID, Content in enumerate(transmission, start = 100):
    if "ERROR" in Content:
        print(f"[ALARM] Packet #[{ID}]: [{Content}]")
    else:
        print(f"[OK] Packet #[{ID}]: Decrypted")
    if ID % 2 == 0 and "ERROR" in Content:
        print(f"[CRITICAL] Packet #[{ID}]: [{Content}]")
        
# pass