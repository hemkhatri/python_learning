# The "System Guardian" Challenge
# Scenario: You are building a monitoring script for a remote server. The script receives a list of data packets (integers). Some packets are corrupted, some are dangerous, and some are standard data.
# The Data:
# packets = [120, 0, 404, 150, 999, 200, 110]
# The Requirements:
# Iterate through the packets list.
# Corrupted Data: If a packet is exactly 0, the "Repair Logic" isn't ready yet. Use a placeholder so the code doesn't break.
# Invalid Data: If a packet is 404, it is an invalid request. Skip it and move to the next packet immediately without printing anything.
# Critical Threat: If a packet is 999, this is a system-level intrusion. Stop all processing and exit the loop immediately.
# Normal Processing: For any other number, print: "Processing packet: [number]"
# The "All Clear": Use the for...else pattern to print "System scan complete: No critical threats detected" only if the loop finishes without hitting a critical threat (999).

packets = [120, 30, 404, 0, 999, 200, 110]
for data in packets:
    if data == 0:
        pass #Repair Mode
    elif data == 404:
        continue #invalid Request
    elif data == 999:
        break #system level intrusion
    else:
        print(f"Processing Packet : [{data}]")
else:
    print("System scan complete: No critical threats detected")