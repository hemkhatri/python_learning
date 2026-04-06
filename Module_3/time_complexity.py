# import time

# start_time = time.perf_counter()

# # def adder(x):
# #     sum = 0
# #     for y in range(1, x + 1):
# #         sum = sum + y
# #     return sum
# # print(adder(100000000))

# end_time = time.perf_counter()
# print(f"Execution time: {end_time - start_time:0.4f} seconds")

# start_time = time.perf_counter()
# def adder_2(x):
#     sum = x * (x + 1) / 2
#     return sum
# print(adder_2(100000000))

# end_time = time.perf_counter()
# print(f"Execution time: {end_time - start_time:0.4f} seconds")


# start = time.perf_counter()
# # print(pow(250,2323))
# end = time.perf_counter()
# print(f"{end - start:0.4f}")
# numbers = [1,2,3,4,5]

# for i in numbers:
#     for j in numbers:
#         print(i, j)

# import sys

# # A range of 1 million numbers
# lazy_range = range(10_000_00)
# # A list of 1 million numbers
# big_list = list(range(1000000))

# print(sys.getsizeof(lazy_range)) # ~48 bytes (Tiny!)
# print(sys.getsizeof(big_list))   # ~8,000,000 bytes (Huge!)



# import time

# try:
#     print("System Started Successfully [1]")
#     while True:
#         print("Working...")
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("\n[!] Terminated the program")
#     print("[✓] System Shutdown Succesfully")

import signal
import sys

def shutdown_handler(sig, frame):
    print(f"\nCaught signal {sig}. Cleaning up...")
    # Add your shutdown logic here
    sys.exit(0)

# Register the handler for SIGINT (which is Ctrl+C)
signal.signal(signal.SIGINT, shutdown_handler)

print("Press Ctrl+C to exit.")
while True:
    pass
