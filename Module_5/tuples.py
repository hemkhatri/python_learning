# tuples = ("Hem", 18, "Good")
# name, roll_no, performance = tuples
# print(performance)

# message = ["2026-09-16", "HemLex", "Hard", "Disk", "Full", "SER:234", "Not Valid"]
# date, company_name, *message, server_name, eligible = message
# print(eligible)

# config = ("192.168.12.1", 25006, "secret_message", "api_key")
# ip, port, _, _ = config
# print(f"Connecting to {ip} with {port} port.....{_}")

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# first, *_, last = numbers
# print(f"first = {first} last = {last}")

# named tuples
# from collections import namedtuple
# Car = namedtuple('Car', ['make', 'model', 'year', 'color'])
# my_car = Car(make = 'Tesla', model= 'fiber', year=2023, color= 'Yellow')

# print(my_car.color)

# from typing Namedtuples
# from typing import NamedTuple
# class User(NamedTuple):
#     id: int
#     username : str
#     is_admin : bool

# currectuser = User(id = 1, username= "myname", is_admin= True)
# print(type(currectuser.count))
# print(currectuser.is_admin)



from typing import NamedTuple

class DBConfig(NamedTuple):
    name : str
    comment : str
    rollno : int
    timeout : float = 30.0

currentuser = DBConfig(name = "Hem", comment= "Hey guys what's up", rollno= 23)
print(currentuser.name, currentuser.timeout)