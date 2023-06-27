import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
  
    def setUp(self):
        self.card1 = Card("Spade", 1)
        self.card2 = Card("Hearts", 2)
        self.card3 = Card("Clubs", 6)
        self.card4 = Card("Diamonds", 9)
        self.card_list = [self.card1, self.card2, self.card3, self.card4]
        self.card_game = CardGame()

    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card1))

    def test_highest_card(self):
        self.assertEqual(self.card4, self.card_game.highest_card(self.card1, self.card4))

    def test_cards_total(self):
        self.assertEqual("You have a total of 18", self.card_game.cards_total(self.card_list))