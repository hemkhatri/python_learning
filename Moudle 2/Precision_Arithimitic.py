# Change these to test your logic!
guest_code = "OPEN_SESAME" # Try changing this to "" or "WRONG_CODE"

# YOUR TASK: Write the 'if' statement using 'and' 
# so that it stops early if guest_code is empty.
guests = ["", None, "OPEN_SESAME"]
if guests[0] == False:
    print("Hello")
else:
    print("hey")
for guest in guests:
    if guest and guest == guest_code:
        print("Welcome to the VIP section!")
    else:
        print("Access Denied.")
