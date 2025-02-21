from time import sleep

from simple_card_game.deck import Deck
from simple_card_game.player import Player


class Table:

    def __init__(self, player: Player, rival: Player, discard_turns: int) -> None:
        self.deck: Deck = Deck()

        self.player: Player = player
        self.rival: Player = rival

        self.discard_turns = discard_turns
        self.turn = 0
        self.SEPARATOR = "=" * 55

        print("Starting game")

    @property
    def in_discard_phase(self):
        return self.turn < self.discard_turns

    def deal_hand(self, n: int):
        sleep(1)

        # Shuffle deck
        self.deck.shuffle_deck()

        # Deal hand
        for _ in range(n):
            self.player.take_card(self.deck.deal_card())
            self.rival.take_card(self.deck.deal_card())

    def deal_card(self):
        self.player.hand.add_card(self.deck.deal_card())

    def discard_turn(self):
        self.turn += 1

        # Display info
        print(self.SEPARATOR)
        print(self.player)

        # Get user input
        inp = input(
            (
                f"(Round {self.turn}/{self.discard_turns}) "
                "Introduce cards to discard (e.g. 0, 3, 4): "
            )
        ).strip()
        if inp:
            discard_idx = [int(x.strip()) for x in inp.split(",")]
        else:
            discard_idx = None

        # Discard hands
        discarded_cards = self.player.discard(discard_idx)
        for _ in range(discarded_cards):
            self.deal_card()
        sleep(1)

    def end_game(self):
        # Show info of last hand
        print(self.SEPARATOR)
        print(self.player)
        print("\nShowing hands...")
        print(self.SEPARATOR)
        sleep(3)

        # Get scores
        rival_hand_name, rival_hand_score = self.rival.get_hand_score()
        player_hand_name, player_hand_score = self.player.get_hand_score()

        # Determine winner
        if player_hand_score > rival_hand_score:
            winner = self.player
            winning_hand = player_hand_name
        elif player_hand_score < rival_hand_score:
            winner = self.rival
            winning_hand = rival_hand_name
        else:
            winner = None
            winning_hand = None

        # Show results
        print(self.rival)
        print(f"\t{rival_hand_name}")
        print("\n\t\t\tvs.\n")
        print(self.player)
        print(f"\t{player_hand_name}")

        if winner:
            print(f"\n\tWinner: {winner.name} with a {winning_hand}")
        else:
            print("\n\tAmazing! There was a draw!")
