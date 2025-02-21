from typing import Literal, TypeAlias


Rank: TypeAlias = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Suit: TypeAlias = Literal["d", "h", "s", "c"]


class Card:

    SUIT_TO_STR: dict[Suit, str] = {
        "d": "Diamonds",
        "h": "Hearts",
        "s": "Spades",
        "c": "Clubs",
    }

    RANK_TO_STR: dict[Rank, str] = {
        1: "Ace",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Jack",
        12: "Queen",
        13: "King",
    }

    RANK_TO_SHORT: dict[Rank, str] = {
        1: "A",
        11: "J",
        12: "Q",
        13: "K",
    }

    def __init__(self, rank: Rank, suit: Suit) -> None:
        self.rank: Rank = rank
        self.suit: Suit = suit

    def __repr__(self) -> str:
        suit_repr = self.SUIT_TO_STR[self.suit]
        rank_repr = self.RANK_TO_STR[self.rank]
        return f"{rank_repr} of {suit_repr}"

    def short_repr(self) -> str:
        return f"{self.RANK_TO_SHORT.get(self.rank, self.rank)}{self.suit.upper()}"
