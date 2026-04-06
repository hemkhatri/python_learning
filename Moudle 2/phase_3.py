# def handle_command(command):
#     match command:
#         case 1:
#             print("Sunday")
#         case 2:
#             print("Monday")
#         case 3:
#             print("Tuesday")
#         case 4:
#             print("Wednesday")
#         case 5:
#             print("Thrusday")
#         case 6:
#             print("Friday")
#         case 7:
#             print("Saturday")
#         case _:
#             print("Unknown Command")

# handle_command(6)
# lists = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday"]



# print(5 >> 1)
# print(5 << 2)
# print(5 << 3)
# print(5 << 3)


# user = None
# if(user.is_admin and user):
#     print("Hello")
# print(bin(5))

# x = 19
# y = 11
# print(f"{x & y:08b}")


# IS_ADMIN = 0b1000
# IS_ACTIVE = 0b0100
# IS_VERIFIED = 0b0010
# IS_PREMIUM = 0b0001

# flags = 0b1001
# is_admin = (flags & IS_ADMIN) > 0

# flags = flags | IS_ACTIVE
# print(flags)
# print(is_admin)
# flags = flags & ~IS_ADMIN
# print(f"{flags:04b}")
# n = 0
# x = "Negative" if n < 0 else "Postive" if n > 0 else "Zero"
# print(x)

data = {
    "name" : "Hem",
    "subject" : "BIT",
    "college" : "Degree Campus", 
    "permission" : "Can_handle"
}
def checker(data):
    if(data):
        if data["name"] == "Hem":
            if data["subject"] == "BIT":
                print("Ok")

def checker_v2(data):
    if not data:
        return "No data found"
    if data["name"] != "Hem":
        return "No matched"
    if data["subject"] != "BIT":
        return "No subject matched"
    return "ok"

print(checker_v2(data))