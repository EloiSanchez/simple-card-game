from hand import Hand


class Player:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.hand: Hand = Hand()

    def discard(self, discard_idx: list[int] | None) -> int:
        if not discard_idx:
            return 0

        discard_idx.sort(reverse=True)
        discarded_cards = len(discard_idx)
        for idx in discard_idx:
            self.hand.discard_card(idx)

        return discarded_cards

    def __repr__(self) -> str:
        value = f"\tPlayer: {self.name}\n\n\tHand:\n"

        value += self.hand.__repr__()

        return value

    def get_hand_score(self) -> tuple[str, int]:
        return self.hand.get_hand_score()
