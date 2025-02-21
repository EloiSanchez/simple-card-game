import unittest

from simple_card_game.card import Card
from simple_card_game.hand import Hand


class TestHand(unittest.TestCase):
    straight = Hand()
    straight.cards = [
        Card(2, "s"),
        Card(6, "s"),
        Card(4, "s"),
        Card(3, "c"),
        Card(5, "s"),
    ]
    straight_flush = Hand()
    straight_flush.cards = [
        Card(2, "s"),
        Card(6, "s"),
        Card(4, "s"),
        Card(3, "s"),
        Card(5, "s"),
    ]
    pair = Hand()
    pair.cards = [
        Card(2, "s"),
        Card(2, "s"),
        Card(4, "c"),
        Card(3, "s"),
        Card(5, "s"),
    ]
    double_pair = Hand()
    double_pair.cards = [
        Card(2, "s"),
        Card(2, "s"),
        Card(4, "c"),
        Card(5, "s"),
        Card(5, "s"),
    ]
    three_of_a_kind = Hand()
    three_of_a_kind.cards = [
        Card(2, "s"),
        Card(2, "s"),
        Card(2, "c"),
        Card(4, "s"),
        Card(5, "s"),
    ]
    four_of_a_kind = Hand()
    four_of_a_kind.cards = [
        Card(2, "s"),
        Card(2, "s"),
        Card(2, "c"),
        Card(2, "s"),
        Card(5, "s"),
    ]
    full_house = Hand()
    full_house.cards = [
        Card(2, "s"),
        Card(2, "s"),
        Card(2, "c"),
        Card(5, "s"),
        Card(5, "s"),
    ]
    flush = Hand()
    flush.cards = [
        Card(2, "s"),
        Card(2, "s"),
        Card(7, "s"),
        Card(5, "s"),
        Card(5, "s"),
    ]
    high_card = Hand()
    high_card.cards = [
        Card(2, "s"),
        Card(3, "c"),
        Card(7, "s"),
        Card(9, "h"),
        Card(5, "s"),
    ]
    hand = Hand()
    hand.cards = [
        Card(2, "s"),
        Card(3, "c"),
        Card(7, "s"),
        Card(9, "h"),
        Card(5, "s"),
    ]

    def test_sorting(self):
        self.straight.sort_by_rank()
        self.assertEqual(self.straight.get_ranks, [2, 3, 4, 5, 6])

    def test_straight(self):
        self.assertEqual(self.straight.get_hand_score()[0], "Straight")

    def test_flush(self):
        self.assertEqual(self.flush.get_hand_score()[0], "Flush")

    def test_pair(self):
        self.assertEqual(self.pair.get_hand_score()[0], "Pair")

    def test_double_pair(self):
        self.assertEqual(self.double_pair.get_hand_score()[0], "Two Pair")

    def test_three_of_a_kind(self):
        self.assertEqual(self.three_of_a_kind.get_hand_score()[0], "Three of a Kind")

    def test_four_of_a_kind(self):
        self.assertEqual(self.four_of_a_kind.get_hand_score()[0], "Four of a Kind")

    def test_straight_flush(self):
        self.assertEqual(self.straight_flush.get_hand_score()[0], "Straight Flush")

    def test_high_card(self):
        self.assertEqual(self.high_card.get_hand_score()[0], "High Card")

    def test_discard_and_draw(self):
        card = self.hand.discard_card(2)
        self.assertEqual((card.rank, card.suit), (7, "s"))
        self.hand.add_card(Card(7, "s"))
        self.assertEqual(len(self.hand.cards), 5)
