# This is the verification for checking the path of file.
# [Method 1]

# import os
# if os.path.exists("error_handling.py"):
#     print("Ok")
# else:
#     print("Error")

# [Method 2]
try:
    with open("error_handling.py") as f:
        print(f.read())
except FileNotFoundError:
    print("File is missing")