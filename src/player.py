from card import Card
from hand import Hand


class Player:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.hand: Hand = Hand()

    def discard(self) -> int:
        inp = input("Introduce cards to discard (e.g. 0, 3, 4): ").strip()

        if not inp:
            return 0

        discard_idx = [int(x.strip()) for x in inp.split(",")]

        discard_idx.sort(reverse=True)
        discarded_cards = len(discard_idx)
        for idx in discard_idx:
            self.hand.discard_card(idx)

        return discarded_cards

    def __repr__(self) -> str:
        value = f"\tPlayer: {self.name}\n\n\tHand:\n"

        value += self.hand.__repr__()

        return value

    def determine_hand(self) -> tuple[str, int]:
        return self.hand.determine_hand()
