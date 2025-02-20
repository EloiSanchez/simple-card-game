from card import Card
from random import shuffle


class Deck:

    def __init__(self) -> None:

        # Build deck
        self.deck: list[Card] = []

        for suit in Card.SUIT_TO_STR.keys():
            for rank in Card.RANK_TO_STR.keys():
                self.deck.append(Card(rank, suit))

    def shuffle_deck(self):
        shuffle(self.deck)

    def deal_card(self) -> Card:
        return self.deck.pop()
