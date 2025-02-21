from simple_card_game.table import Table
from simple_card_game.player import Player


class Game:

    def __init__(self, discard_turns: int):
        # Get players
        self.player = Player(input("What is your name? "))
        self.rival = Player(input("What is the name of your rival? "))

        # Instantiate table/dealer
        self.table = Table(self.player, self.rival, discard_turns=discard_turns)

        self.table.deal_hand(5)

    def play(self):
        # Start discard phase
        while self.table.in_discard_phase:
            self.table.discard_turn()

        # Start showing phase
        self.table.end_game()
