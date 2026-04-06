READ = 0b0100 #4
WRITE = 0b0010 #2
EXECUTE = 0b0001 #1

permissions = int(input("permission= "))
# if 0 > permissions > 7:
if permissions < 0 or permissions > 7:
    print("INVALID PERMISSION CODE")

else:
    task = input("command= ")
    match task:
        case "read":
            if (permissions & READ) != 0:
                print("ACCESS GRANTED")
            else:
                print("ACCESS DENIED")

        case "edit":
            if (permissions & WRITE) != 0:
                print("ACCESS GRANTED")
            else:
                print("ACCESS DENIED")

        case "run":
            if (permissions & EXECUTE) != 0:
                print("ACCESS GRANTED")
            else:
                print("ACCESS DENIED")
        case _:
            print("INVALID COMMAND")
