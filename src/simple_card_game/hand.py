from simple_card_game.card import Card, Rank


class Hand:

    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.index: int = 0

    @property
    def get_ranks(self) -> list[Rank]:
        return [card.rank for card in self.cards]

    def sort_by_rank(self):
        sorted_cards = [
            i[1] for i in sorted(zip(self.get_ranks, self.cards), key=lambda x: x[0])
        ]
        self.cards = sorted_cards

        return self.cards

    def __repr__(self) -> str:
        value = "\t" + "┌     " * 5 + "\n\t"
        for card in self:
            value += "".join(f"{card.short_repr():<}  ".rjust(6))
        value += "\n\t" + "     ┘" * 5 + "\n"

        return value

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.cards[self.index]
        except IndexError:
            self.index = 0
            raise StopIteration
        self.index += 1
        return result

    def add_card(self, card: Card):
        self.cards.append(card)

    def discard_card(self, idx: int):
        return self.cards.pop(idx)

    def get_hand_score(self) -> tuple[str, int]:
        # Sort cards by rank
        self.sort_by_rank()

        # Counter variables
        pairs = 0
        trios = 0
        four_of_a_kinds = 0
        straight = True
        flush = True

        # First card
        previous_card = self.cards[0]
        highest_card = self.cards[0]

        # Get hand types
        equal_card = 0
        for card in self.cards[1:]:

            # Update highest card
            if highest_card.rank < card.rank:
                highest_card = card

            # Repeated cards?
            if previous_card.rank == card.rank:
                equal_card += 1
            else:
                equal_card = 0

            if equal_card == 1:
                pairs += 1
            elif equal_card == 2:
                pairs -= 1
                trios += 1
            elif equal_card == 3:
                trios -= 1
                four_of_a_kinds += 1

            # Straight?
            if not (
                previous_card.rank + 1 == card.rank
                or (previous_card.rank == 1 and card.rank == 10)
            ):
                straight = False

            # Flush?
            if not (previous_card.suit == card.suit):
                flush = False

            previous_card = card

        # Get hand score
        card_values = sum(x if x != 1 else 14 for x in self.get_ranks)
        if flush and straight:
            hand_name = "Straight Flush"
            score = 1000
        elif four_of_a_kinds == 1:
            hand_name = "Four of a Kind"
            score = 900
        elif trios == 1 and pairs == 1:
            hand_name = "Full House"
            score = 800
        elif flush:
            hand_name = "Flush"
            score = 700
        elif straight:
            hand_name = "Straight"
            score = 600
        elif trios == 1:
            hand_name = "Three of a Kind"
            score = 500
        elif pairs == 2:
            hand_name = "Two Pair"
            score = 400
        elif pairs == 1:
            hand_name = "Pair"
            score = 300
        else:
            hand_name = "High Card"
            score = max(self.get_ranks)

        return hand_name, score + card_values
