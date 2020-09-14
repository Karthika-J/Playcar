#task = ""
started = False
while True :
    task = input("> ").lower()
    if task == "start":
        if started :
            print("Car already started! ")
        else:
            started = True
            print("Car started ! Ready to go !!")
            print("Car started ! Ready to go !!")
    elif task == "stop":
        if not started :
            print("Car is already stopped!!")
        else:
            started = False
            print("Car stopped!")
    elif task == "help":
        print("""
Start  -- To start the car
Stop   -- To stop the car
Help   -- To get all commands
quit   -- To quit out of game""")
    elif task == "quit":
        break
    else:
        print("Sorry I don't understand that")

