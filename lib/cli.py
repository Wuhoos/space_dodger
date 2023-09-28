# lib/cli.py
from models.model_1 import main
from helpers import (
    exit_program,
    initialize,
    get_all_player,
    delete_player
)


def main_menu():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            main()
            break
        elif choice == '2':
            get_all_player()
        elif choice == '3':
            delete_player()
        
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Login")
    print('2. Lists of Players')
    print('3. Delete player by id')


if __name__ == "__main__":
    initialize()
    main_menu()
