from player import Player
import pokemon
from time import sleep

def player_options():
    return False

def start_game():
    playing = True
    print("Hello, what is your name?")
    name = input()

    sleep(1)

    print(f"\nNice to meet you {name}. Here's some pokeballs. Go out there and catch a few pokemon.\n")
    pc = Player(name)

    sleep(1)
    
    print("Pokeballs added\n\n")
    while playing:
        sleep(1)
        playing = player_options()
    print("Bye!")

start_game()