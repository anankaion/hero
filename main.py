from commands import *
from characters import *

commands = [""]
player = Player

print("Welcome! You are the hero. You decide. What will it be?")
print("(Enter help for help")

while commands[0] != "exit":
    print(">", end="")
    commands = input().split(" ")

    if commands[0] == "help":
        get_help()

    elif commands[0] == "walk":
        if len(commands) == 2:
            walk(player, commands[1])
        elif len(commands) > 2:
            print("Too many directions at once.")
        else:
            print("Where to go?")

    elif commands[0] == "explain":
        explain(player)

    elif commands[0] == "fight":
        fight(player)

    elif commands[0] == "exit":
        pass

    else:
        print("Command not included.")
