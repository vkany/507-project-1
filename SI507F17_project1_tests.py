# Do not change import statements.
import unittest
from SI507F17_project1_cards import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in the code description
# file works as that file says.
# If you have correctly written the tests,  at least 3 tests should fail. If
# more than 3 tests fail, it should be because multiple of the test methods
# address the same problem in the code.
# You may write as many TestSuite subclasses as you like,  but you should try
# to make these tests well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########


class CardTest(unittest.TestCase):

    def setUp(self):
        self.card = Card(2,  13)

    def test1(self):  # checking correst suit_names
        self.assertEqual(type(self.card.suit_names), list)

    def test2(self):
        self.assertEqual(self.card.suit, 'Hearts',  'check value of')

    def test3(self):
        self.assertEqual(self.card.rank,  "King")

    def test4(self):
        self.assertEqual(type(self.card.rank_num), int)

    def test5(self):
        self.assertEqual(str(self.card),  'King of Hearts')
        # The Card class has a string method,  which should return a string
        # e.g. "Ace of Spades" or "3 of Clubs",  etc.

    def tearDown(self):
        self.card = Card(2,  13)


class DeckTest(unittest.TestCase):

    def setUp(self):
        self.d = Deck()
        self.card = Card(2, 13)

    def test6(self):
        self.assertEqual(type(self.d.cards), list)

    def test7(self):
        self.assertTrue(self.d.pop_card(),  self.card not in self.d.cards)

    def test8(self):
        d_string = str(self.d)
        d_list = d_string.split('\n')
        self.assertEqual(len(d_list),  52)

    def test9(self):
        original_deck = str(self.d)
        self.d.shuffle()
        shuffle_deck = str(self.d)
        self.assertTrue(original_deck != shuffle_deck)

    def test10(self):
        self.d.replace_card(self.card)
        self.assertTrue(len(self.d.cards) == 52)

    def test11(self):
        poppped_card = self.d.pop_card()
        original_deck = str(self.d)
        self.d.shuffle()
        shuffle_deck = str(self.d)
        self.d.sort_cards()
        sort_deck = str(self.d)
        # print (original_deck)
        # print("-------------------")
        # print (sort_deck)
        self.assertTrue(original_deck == sort_deck)

    def test12(self):
        original_deck = str(self.d)
        self.d.deal_hand(7)
        new_deck = str(self.d)
        self.assertTrue(original_deck == new_deck)


class WarGameTest(unittest.TestCase):

    def setUp(self):
        self.war = play_war_game(testing=True)

    def test13(self):
        self.assertEqual(type(self.war), tuple)


class SongTest(unittest.TestCase):

    def setUp(self):
        self.song = show_song()
        self.song2 = show_song("Shake it off")

    def test14(self):
        self.assertEqual(self.song2.artist, "Taylor Swift")

    def test15(self):
        self.assertEqual(str(self.song),
            "{} by {} on {} whose URL is {}".format(
            self.song.track, self.song.artist,
            self.song.album, self.song.track_url))


unittest.main(verbosity=2)
