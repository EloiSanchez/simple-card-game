from time import sleep
from table import Table
from player import Player


SEPARATOR = "=" * 50
MAX_TURNS = 3


def main():

    # Get players
    player = Player(input("What is your name? "))
    rival = Player(input("What is the name of your rival? "))

    # Instantiate table/dealer
    table = Table(player, rival)

    print("Starting game")
    sleep(1)

    table.deal_hand(5)

    # Start discard phase
    turn = 0
    while turn < MAX_TURNS:
        turn += 1
        print(SEPARATOR)
        print(player)
        discarded_cards = player.discard()
        for _ in range(discarded_cards):
            table.deal_card()
            sleep(1)

    print(SEPARATOR)
    print(player)

    # Start showing phase
    print("\nShowing hands...")
    print(SEPARATOR)
    sleep(2)
    table.end_game()
    print(SEPARATOR)


if __name__ == "__main__":
    main()
