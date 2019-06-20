from characters import Rat


# explains all the available commands
def get_help():
    print("Commands in this game:")
    print("exit\texits the game")
    print("explain\texplains the situation")
    print("walk\twalk in a direction")
    print("fight\tfight a monster")
    print("help\tview this menu")


# walk in a certain direction, relative from where you are
def walk(player, direction):
    if player.whereami == "start":
        if direction == "in":
            print("You go in.")
            player.whereami = "hall"

        else:
            print("You can only go in")

    elif player.whereami == "hall":
        if direction == "north":
            print("You go north into the next room.")
            player.whereami = "fightroom1"

        elif direction == "south":
            print("You went back outside.")
            player.whereami = "start"

        elif direction == "east":
            print("You go east into the next room.")
            player.whereami = "emptyroom"

        elif direction == "west":
            print("You go west into the next room.")
            player.whereami = "merchantroom"

        else:
            print("Not a direction.")


# explain your surroundings
def explain(player):
    if player.whereami == "start":
        print("You are at the beginning of your journey.")

    elif player.whereami == "hall":
        print("You stand in a big hall. Doors are to all 4 sides.")

    elif player.whereami == "fightroom1":
        print("You look around and spot a nasty rat. It is blocking the next entrance. You will probably have to "
              "fight it.")


def fight(player):
    if player.whereami == "fightroom1":
        fight_specific(player, Rat)


def fight_specific(player, enemy):
    while player.health > 0 and enemy.health > 0:
        enemy.health -= player.attack
        print("Player attacked enemy with " + str(player.attack) + " damage.")

        if enemy.health > 0:
            player.health -= enemy.attack
            print("Enemy attacked Player with " + str(enemy.attack) + " damage.")
        else:
            print("Player killed enemy.")
