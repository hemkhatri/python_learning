# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# x = zip(a, b)
# print(list(x))

# males = ["Ram", "Shyam", "Hari", "Myakuri"]
# females = ["Kristina", "Sita", "Sushma", "Eendera"]

# couples_name = zip(males, females)
# # for name in couples_name:
# #     print(name)
# a = [('Ram', 'Kristina'), ('Shyam', 'Sita'), ('Hari', 'Sushma'), ('Myakuri', 'Eendera')]
# # for x in couples_name:
#     # print(x)

# m, f = zip(*a)
# print(m, f)

# dict = {
#     "name" : "Hem",
#     "class" : "BIT",
#     "roll_no" : 27,
#     "mobile_no" : 9815205677
# }
# key = dict.keys()
# values = dict.values()
# # print(dict.values())
# pair = zip(key, values)
# print(list(pair))


#ALL exercises upto now

# You are managing a Global Data Center and need to run a health check. You have three parallel data streams: one for Server IDs, one for Power Consumption (in Watts), and one for Thermal Status.
# The Mission
# Write a script that iterates through all three streams simultaneously to generate a status report.
# Your constraints:
# Use zip() to pair the three lists.
# Use enumerate() to assign a Rack Number to each set, starting at Rack 500.
# The "Efficiency Check": Use a for...else pattern. If you find a server consuming more than 450W, print: [CRITICAL] Rack [ID]: [Server] ALERT - HIGH POWER ([Watts]W). Immediately stop the entire health check.
# The "Clean Check": If the loop completes without finding any high-power servers, print: [COMPLETE] All racks in this sector are within safety limits.
# The "Maintenance Skip": If a server's thermal status is "OFFLINE", skip that specific rack entirely and move to the next one without printing anything for it.
# The Data:
# python
# servers = ["Srv-Alpha", "Srv-Beta", "Srv-Gamma", "Srv-Delta", "Srv-Epsilon"]
# power_usage = [210, 350, 480, 120, 310]
# thermal_status = ["STABLE", "STABLE", "STABLE", "OFFLINE", "STABLE"]


servers = ["Srv-Alpha", "Srv-Beta", "Srv-Gamma", "Srv-Delta", "Srv-Epsilon"]
power_usage = [210, 350, 480, 120, 310]
thermal_status = ["STABLE", "STABLE", "STABLE", "OFFLINE", "STABLE"]

# global_view = zip(servers, power_usage, thermal_status)
# for rack_no, view in enumerate(global_view):
#     print(rack_no, view)


for rack_no, (server, power_use, thermal_cond) in enumerate( zip( servers, power_usage, thermal_status), start = 500):
    if power_use > 450:    
        print(f"[CRITICAL] Rack [{rack_no}]: [{server}] ALERT - HIGH POWER ([{power_use}]W)")
        # break
    elif thermal_cond == "OFFLINE":
        continue
    else:
        print()
else:
    print("[COMPLETE] All racks in this sector are within safety limits.")