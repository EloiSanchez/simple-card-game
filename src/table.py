from deck import Deck
from player import Player


class Table:

    def __init__(self, player: Player, rival: Player) -> None:
        self.deck: Deck = Deck()

        self.player: Player = player
        self.rival: Player = rival

    def deal_hand(self, n: int):
        self.deck.shuffle_deck()

        for _ in range(n):
            self.player.hand.add_card(self.deck.deal_card())
            self.rival.hand.add_card(self.deck.deal_card())

    def deal_card(self):
        self.player.hand.add_card(self.deck.deal_card())

    def end_game(self):

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
