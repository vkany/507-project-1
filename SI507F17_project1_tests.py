## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
class CardTest(unittest.TestCase):

    def setUp(self):
        self.card = Card(2, 13)

    def test1(self): # #checking correst suit_names
        # self.assertEqual(self.card.rank_num, 1, 'check values')
        self.assertEqual(type(self.card.suit_names),list)

    def test2(self):
        self.assertEqual(self.card.suit,'Hearts', 'check value of ')

    def test3(self):
        self.assertEqual(self.card.rank,"King")

    def test4(self):
        self.assertEqual(type(self.card.rank_num),int)

    def test5(self):
        self.assertEqual(str(self.card), 'King of Hearts') #The Card class has a string method, which should return a string e.g. "Ace of Spades" or "3 of Clubs", etc.

class DeckTest(unittest.TestCase):

    def setUp(self):
        self.d = Deck()

    def test6(self):
        self.assertEqual(type(self.d.cards), list)

    # def test8(self):


unittest.main(verbosity=2)
