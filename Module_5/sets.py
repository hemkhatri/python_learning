# my_set = {1, 2, 3, 4, 5, "hello", 7, 8, 9}
# print(23 in my_set)
# my_set.add(2)
# # is_available = "True" if x in my_set else "False"
# print(23 in my_set)
# print((my_set))


# admins = {"alice", "bob", "charlie"}
# developers = {"bob", "david", "alice"}

# print(developers ^ admins)
# print(admins - developers)


# raw_data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 5, 4, 5, 7, 8, 34, 4, 3, 2, 43, 5, 1, 2, 4, 5, 6, 7, 4, 3, 2, 1, 4, 5, 6, 7, 8, 4, 3, 2, 3, 4]
# simplified_data = list(set(raw_data))
# print(simplified_data) 


# def process_tags(user_input: list) -> list:
#     # 1. Clean whitespace and lowercase everything
#     clean_input = [tag for tag in user_input]
    
#     # 2. Remove duplicates but KEEP the user's preferred order
#     unique_tags = list(dict.fromkeys(clean_input))
    
#     return unique_tags

# # Usage
# raw_tags =  [1, 2, 3, 4, 5, 5, 6, 7, 8, 5, 4, 5, 7, 8, 34, 4, 3, 2, 43, 5, 1, 2, 4, 5, 6, 7, 4, 3, 2, 1, 4, 5, 6, 7, 8, 4, 3, 2, 3, 4]
# final_tags = process_tags(raw_tags)

# print(final_tags)
# # Output: ['python', 'coding', 'programming']





# def process_tags(user_input: list) -> list:
#     # 1. Convert to string, clean whitespace, and lowercase
#     # This handles both numbers and strings safely
#     clean_input = [str(tag).strip().lower() for tag in user_input]
    
#     # 2. Remove duplicates while keeping order
#     unique_tags = list(dict.fromkeys(clean_input))
    
#     return unique_tags

# # Use strings if that is your intended final output format
# raw_tags = [" Python ", "coding", "PYTHON", "Programming", "coding"]
# final_tags = process_tags(raw_tags)

# print(final_tags) 
# # Output: ['python', 'coding', 'programming']

# print(f"There is a ")




# import sys

# mylist= [1, 2, 3, 4, "Hello"]
# my_tuple = (1, 2, 3, 4, "Hello")
# my_set = {1, 2, 3, 4, "Hello"}

# print(f"{sys.getsizeof(my_tuple)}")
# print(f"{sys.getsizeof(mylist)}")
# print(f"{sys.getsizeof(my_set)}")


# Example: Using a frozenset to map a combination of ingredients to a recipe
# ingredients = frozenset(['flour', 'sugar', 'eggs'])
# recipes = {ingredients: "Basic Cake"}

# # You can look it up with a new frozenset containing the same items
# search_key = frozenset(['sugar', 'eggs', 'flour'])
# print(recipes[search_key])  # Output: Basic Cake




# normal_set = {1, 2, 3, 4}
# normal_set.add(5)
# forzen = frozenset([1, 2, 3, 4, 5])
# print(type(normal_set))
# print(normal_set)
# print(type(forzen))



# dict = {
# frozenset({1, 2, 3}) : "Admin"
# }
# print(dict[frozenset({1, 2, 3})])

# key1 = frozenset([1, 2, 3, 4])
# key2 = frozenset([2, 1, 4, 3, 2, 1])

# print(key1 == key2)


# sets = {1, 2, 3, 4, 5}
# sets.add(7)
# sets.clear()
# print(sets)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# # x.discard("apple")
# print(x.intersection_update(y))
# print(x.issubset(y))
# # x.difference_update(y)

# print(x)



# add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, issubset, issuperset, pop,  remove, symmetric_difference_update, union, update

# add, clear, copy, difference, difference_update, discard, intersection, intersection_update, indisjoint, issubset, issuperset, pop , remove, symmetrical_difference_update, union, update


# add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, issubset, issuperset, pop, remove, symmetrical_difference_update, union, update

# add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, issubset, issuperset, pop, remove, symmetrical_difference_update, union, update,


# a = ["add", "remove", "difference", "difference_update", "copy", "discard", "intersection", "intersection_update", "isdisjoint", "issubset", "issuperset", "pop", "remove", "symmetrical_differnce_update", "union", "update"]
# count = 0
# for ad in a:
#     count += 1
# print(count)



# sets = """
# add, clear, copy, differnce, difference_update, discard, intersection, intersection_update, issubset, issuperset, isdisjoint, pop, remove, symmetrical_difference_update, union, update 
# """
# print("Hello")


# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# set1.add(24)
# set1.clear()
# print(set1.intersection(set2))
# set1.intersection_update(set2)

# set2.pop()
# print(set1.isdisjoint(set2))
# set1.remove(1)
# print(set1)
# print(set2)




# You have a set of required_skills = {"Python", "SQL", "AWS"}.
# You have an applicant with applicant_skills = {"Java", "SQL", "C++"}.
# The Challenge:
# You need to update the applicant_skills set so that it ends up containing only the skills the applicant was missing from the requirements, plus the skills they already had that weren't required at all.
# Basically, you want to remove what they already correctly matched ("SQL") and add what they are missing ("Python", "AWS"), while keeping their extra skills ("Java", "C++").
# The Question:
# Which single method from your list can perform this exact "flip" on the applicant_skills set in one line?


# required_skills = {"Python", "SQL", "AWS"}
# applicant_skills = {"Java", "SQL", "C++"}

# applicant_skills.update(required_skills)
# print(applicant_skills)


# Starting with a frozenset
# fs1 = frozenset([1, 2, 3])

# Other iterables (they don't have to be frozensets)
# set_a = {3, 4, 5}
# list_b = [5, 6, 7]

# Unioning multiple items at once
# result = fs1.union(set_a, list_b)

# print(result)
# Output: frozenset({1, 2, 3, 4, 5, 6, 7})



# Extended Requirements: High-Speed Firewall Simulator
# To transition this from a simple script to a robust architectural simulation, your build should satisfy the following expanded specifications:
# 1. Data Generation Module
# Unique Blacklist Generation: Programmatically generate exactly 1,000 unique IP addresses (formatted as strings, e.g., "192.168.1.1"). These must be stored in a Set for the primary filter.
# Mirror List: Create a second object containing the exact same 1,000 IPs, but stored as a List. This will be used as the "inefficient" comparison control.
# Traffic Simulation: Generate a "Live Log" containing 50,000 incoming traffic entries.
# Each entry must be a Tuple formatted as (float_timestamp, ip_string, status_string).
# The status_string should be initialized as "PENDING".
# Ensure a specific percentage (e.g., 5%) of these 50,000 IPs are intentionally pulled from your Blacklist to ensure there are "hits" to find.
# 2. The Filtering Engine (Dual Implementation)
# The Architect’s Path (Set Intersection): Implement a filter that identifies all blocked traffic by finding the common elements between the unique IPs in your traffic log and the Blacklist set.
# The Junior Developer’s Path (Linear Scan): Implement a secondary filter that iterates through the traffic log and checks for each IP’s existence within the List version of the blacklist.
# The Purge: Create a "Clean Traffic" collection using a List Comprehension that excludes any entry whose IP exists in the Blacklist.
# 3. Analytics and Performance Metrics
# Microsecond Precision: Capture the system start and end times for both the Set-based filtering and the List-based filtering.
# Comparative Ratio: Calculate the "Speedup Factor" (Time taken by List / Time taken by Set).
# Memory Footprint Awareness: (Optional/Conceptual) Note the behavior of the system as the traffic volume scales from 50,000 to 100,000 entries.
# 4. Output and Verification
# Data Integrity: The simulator must output the total count of blocked packets found versus clean packets allowed.
# Validation: Both the Set-based and List-based filters must return the exact same count of blocked IPs to prove that efficiency did not compromise accuracy.
# Final Report: Display a formatted summary showing the total processing time for each method and the final efficiency verdict.
# Would you like me to clarify any of these arc

# h = {1, 2, 3}
# print(len(h))
# ip_address = {f"192.168.1.{ip}" for ip in range(1000)}
# lists = list(ip_address)

# # while len(ip_address) <= 10:
# #     for ip in range(10):
# #         ip_address.add(f"192.168.1.{ip}")
# # # ip_address = set(lists)
# print(lists)


import time
import random

# --- STEP 1: DATA GENERATION (The Assembly Line) ---
print("Generating 1,000 Blacklisted IPs...")
# We use a set comprehension to create 1,000 unique IP strings
blacklist_set = {f"192.168.1.{i}" for i in range(1000)}
blacklist_list = list(blacklist_set)  # The "Mirror List" for the speed test

print("Simulating 50,000 Traffic Logs...")
traffic_log = []
for _ in range(50000):
    # 5% chance to pick a blacklisted IP, 95% chance for a random "safe" one
    if random.random() < 0.05:
        ip = random.choice(blacklist_list)
    else:
        ip = f"10.0.0.{random.randint(0, 255)}"
    
    # Each entry is a TUPLE: (timestamp, ip, status)
    entry = (time.time(), ip, "PENDING")
    traffic_log.append(entry)

# --- STEP 2: THE JUNIOR DEVELOPER'S ENGINE (List Search) ---
print("\nRunning Junior Developer Engine (List Search)...")
start_list = time.time()

blocked_count_list = 0
for entry in traffic_log:
    # This is the slow part: searching a LIST takes O(n) time
    if entry[1] in blacklist_list:
        blocked_count_list += 1

end_list = time.time()
list_time = end_list - start_list

# --- STEP 3: THE ARCHITECT'S ENGINE (Set Intersection) ---
print("Running Architect Engine (Set Intersection)...")
start_set = time.time()

# Extract only IPs from the log using a set comprehension
log_ips = {entry[1] for entry in traffic_log}

# Architect move: Use Set Intersection to find common IPs instantly
blocked_ips = log_ips.intersection(blacklist_set)

# Use List Comprehension for "Clean Traffic"
clean_traffic = [entry for entry in traffic_log if entry[1] not in blacklist_set]

end_set = time.time()
set_time = end_set - start_set

# --- STEP 4: EFFICIENCY REPORT ---
print("\n" + "="*30)
print("      EFFICIENCY REPORT")
print("="*30)
print(f"Total Traffic Processed: {len(traffic_log)}")
print(f"Blocked Packets Found:   {len(blocked_ips)}")
print(f"Clean Packets Allowed:   {len(clean_traffic)}")
print("-" * 30)
print(f"List Search Time:        {list_time:.5f} seconds")
print(f"Set Intersection Time:   {set_time:.5f} seconds")

if set_time > 0:
    speedup = list_time / set_time
    print(f"Verdict: Set is {speedup:.1f}x faster than List!")
print("="*30)
