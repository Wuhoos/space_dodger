# lib/helpers.py
from models.model import Player, Score

def initialize():
    Player.create_table()
    Player.get_all()
    Score.create_table()
    Score.get_all()
    

def exit_program():
    print("Goodbye!")
    exit()



def get_all_player():
    if len(Player.all) == 0:
        print("Error: NO PLAYER EXISIT!")
    else:
        for player in Player.all:
            print(player)
        print('Retrieved Players INFO')

def delete_player():
    if len(Player.all) == 0:
        print('No Player to delete')
    else:
        player = search_by_id()
        player.delete()
        print('Player deleted.')
        keyboard = input("* return to continue */n")

def search_by_id():
    print(f"Enter the id for the Player you want")
    id = input("> ")

    if id.isdigit():
        player = Player.find_by_id(int(id))
    else:
        player = None
    
    while not player:
        print('Error: Player not found')
        print(f"Enter the id for the Player you want")
        id = input("> ")

        if id.isdigit():
            player = Player.find_by_id(int(id))
        else:
            player = None
    
    return player