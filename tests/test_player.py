import sys
import unittest

sys.path.insert(1, "src")

from card import Card
from hand import Hand
from player import Player


class TestPlayer(unittest.TestCase):
    player = Player("Test")
    player.hand = Hand()
    player.hand.cards = [
        Card(2, "s"),
        Card(6, "s"),
        Card(4, "s"),
        Card(3, "c"),
        Card(5, "s"),
    ]

    def test_discard(self):
        self.assertEqual(self.player.discard(None), 0)
        self.assertEqual(len(self.player.hand.cards), 5)
        self.assertEqual(self.player.discard([2, 3]), 2)
        self.assertEqual(len(self.player.hand.cards), 3)
