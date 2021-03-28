import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Diamonds", 4)
        self.cardgame = CardGame()


    def test_can_check_for_ace__ace(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self.card1))

    def test_can_check_for_ace__not_ace(self):
        self.assertEqual(False, self.cardgame.check_for_ace(self.card2))

    def test_can_return_highest_card(self):
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card1, self.card2))     

    def test_can_return_cards_total(self):
        self.assertEqual("You have a total of 5", self.cardgame.cards_total(self.card1, self.card2))

