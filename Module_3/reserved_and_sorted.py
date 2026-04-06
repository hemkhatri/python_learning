# marks = [24, 35, 6, 7, 34, 6, 3, 6]
# # print(sorted(marks)
# sorted_marks = sorted(marks, reverse=False)
# print(sorted_marks)

# reversed_marks = reversed(marks)
# print(list(reversed_marks))
# print(marks)

# The Challenge: The Multi-Stream Log Auditor
# Scenario:
# You are developing a diagnostic tool for a dual-sensor monitoring system. You have two data streams recorded at the same intervals: timestamps (strings) and power_readings (integers representing Watts).
# The Task:
# Write a script that processes these two lists to identify a specific system "event." An event is defined as any sequence where the power reading exceeds 500W for at least three consecutive cycles.
# Requirements:
# Parallel Processing: Iterate through both timestamps and power_readings simultaneously without using index-based manual lookups (e.g., range(len(x))).
# No Mutation: You must generate a report of the last 5 readings of the day, but they must be displayed in descending order of power consumption (highest wattage first), without altering the original order of your source lists.
# Search Logic: Use a for...else block to search the data for a "Critical Surge" (defined as any reading over 900W).
# If found, print the timestamp and value, then stop searching immediately.
# If the entire log is scanned and no such surge exists, print a "System Nominal" status message.
# Formatting: For every reading processed, print a log line formatted as:
# [Index] Time: <timestamp> | Load: <power>W
# Mock Data to Use:
# python
# timestamps = ["10:00", "10:01", "10:02", "10:03", "10:04", "10:05"]
# power_readings = [450, 520, 950, 480, 300, 720]

# timestamps = ["10:00", "10:01", "10:02", "10:03", "10:04", "10:05"]
# power_readings = [450, 520, 950, 480, 300, 720]

# for index, (timestamp, power_reading) in enumerate(zip(timestamps, sorted(power_readings, reverse= True)), start=1):
#     if(power_reading > 900):
#         print("Critical Surge")
#         break
#     print(f"[{index}] Time : {timestamp} | Load : {power_reading}W")
# else:
#     print("System Nominal")
