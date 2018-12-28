from time import *
# Health Management System
client_list = {1: "Deepak", 2: "Shubham",3:"Anand"}
lock_list = {1: "Exercise", 2: "Diet"}


def getdate():
    a=asctime(localtime(time()))
    return a

try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input())

    print("Selected Client : ", client_list[client_name], "\n", end="")

    print("Press 1 for Lock")
    print("Press 2 for Retrieve")
    op = int(input())

    if op is 1:
        for key, value in lock_list.items():
            print("Press", key, "to lock", value, "\n", end="")
        lock_name = int(input())
        print("Selected Job : ", lock_list[lock_name])
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")
        k = 'y'
        while (k is not "n"):
            print("Enter", lock_list[lock_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()
    elif op is 2:
        for key, value in lock_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        lock_name = int(input())
        print(client_list[client_name], "-", lock_list[lock_name], "Report :", "\n", end="")
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Wrong Input !!!")
