import unittest
from battleship.test_board import test_board
from Blackjack.testBlackjack import (
    TestCards,
    TestBets,
    TestHands,
)
from Generala.test_categories import test_categories
from truco.test_cartas import TestCartas


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(test_board))
    test_suite.addTest(unittest.makeSuite(TestCards))
    test_suite.addTest(unittest.makeSuite(TestBets))
    test_suite.addTest(unittest.makeSuite(TestHands))
    test_suite.addTest(unittest.makeSuite(test_categories))
    test_suite.addTest(unittest.makeSuite(TestCartas))
    return test_suite


if __name__ == "__main__":
    unittest.main()