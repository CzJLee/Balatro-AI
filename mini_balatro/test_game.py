"""Unit tests for mini_balatro."""

import unittest
import mini_balatro
from mini_balatro import deck
import parameterized


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = mini_balatro.Game(seed=0)

    @parameterized.parameterized.expand(
        [
            parameterized.param(
                "Flush Five",
                cards=[
                    deck.Card(1, "heart"),
                    deck.Card(1, "heart"),
                    deck.Card(1, "heart"),
                    deck.Card(1, "heart"),
                    deck.Card(1, "heart"),
                ],
                expected="Flush Five",
                num_cards=5,
            ),
            parameterized.param(
                "Flush House",
                cards=[
                    deck.Card(4, "diamond"),
                    deck.Card(4, "diamond"),
                    deck.Card(4, "diamond"),
                    deck.Card(10, "diamond"),
                    deck.Card(10, "diamond"),
                ],
                expected="Flush House",
                num_cards=5,
            ),
            parameterized.param(
                "Five of a Kind",
                cards=[
                    deck.Card(11, "diamond"),
                    deck.Card(11, "diamond"),
                    deck.Card(11, "diamond"),
                    deck.Card(11, "diamond"),
                    deck.Card(11, "spade"),
                ],
                expected="Five of a Kind",
                num_cards=5,
            ),
            parameterized.param(
                "Straight Flush",
                cards=[
                    deck.Card(12, "club"),
                    deck.Card(13, "club"),
                    deck.Card(11, "club"),
                    deck.Card(1, "club"),
                    deck.Card(10, "club"),
                ],
                expected="Straight Flush",
                num_cards=5,
            ),
            parameterized.param(
                "Straight Flush with A2345",
                cards=[
                    deck.Card(1, "heart"),
                    deck.Card(2, "heart"),
                    deck.Card(3, "heart"),
                    deck.Card(4, "heart"),
                    deck.Card(5, "heart"),
                ],
                expected="Straight Flush",
                num_cards=5,
            ),
            parameterized.param(
                "Four of a Kind",
                cards=[
                    deck.Card(12, "spade"),
                    deck.Card(12, "heart"),
                    deck.Card(12, "club"),
                    deck.Card(12, "diamond"),
                    deck.Card(5, "spade"),
                ],
                expected="Four of a Kind",
                num_cards=4,
            ),
            parameterized.param(
                "Four of a Kind 4 cards",
                cards=[
                    deck.Card(12, "spade"),
                    deck.Card(12, "heart"),
                    deck.Card(12, "club"),
                    deck.Card(12, "diamond"),
                ],
                expected="Four of a Kind",
                num_cards=4,
            ),
            parameterized.param(
                "Full House",
                cards=[
                    deck.Card(7, "spade"),
                    deck.Card(7, "heart"),
                    deck.Card(7, "club"),
                    deck.Card(2, "diamond"),
                    deck.Card(2, "spade"),
                ],
                expected="Full House",
                num_cards=5,
            ),
            parameterized.param(
                "Flush",
                cards=[
                    deck.Card(2, "club"),
                    deck.Card(4, "club"),
                    deck.Card(6, "club"),
                    deck.Card(8, "club"),
                    deck.Card(10, "club"),
                ],
                expected="Flush",
                num_cards=5,
            ),
            parameterized.param(
                "Flush with pair",
                cards=[
                    deck.Card(2, "club"),
                    deck.Card(2, "club"),
                    deck.Card(6, "club"),
                    deck.Card(8, "club"),
                    deck.Card(10, "club"),
                ],
                expected="Flush",
                num_cards=5,
            ),
            parameterized.param(
                "Flush with three of a kind",
                cards=[
                    deck.Card(2, "club"),
                    deck.Card(2, "club"),
                    deck.Card(2, "club"),
                    deck.Card(8, "club"),
                    deck.Card(10, "club"),
                ],
                expected="Flush",
                num_cards=5,
            ),
            parameterized.param(
                "Straight",
                cards=[
                    deck.Card(4, "spade"),
                    deck.Card(5, "club"),
                    deck.Card(6, "heart"),
                    deck.Card(7, "club"),
                    deck.Card(8, "club"),
                ],
                expected="Straight",
                num_cards=5,
            ),
            parameterized.param(
                "Straight with A2345",
                cards=[
                    deck.Card(3, "heart"),
                    deck.Card(2, "club"),
                    deck.Card(5, "club"),
                    deck.Card(4, "club"),
                    deck.Card(1, "spade"),
                ],
                expected="Straight",
                num_cards=5,
            ),
            parameterized.param(
                "Straight with AKQJ10",
                cards=[
                    deck.Card(10, "heart"),
                    deck.Card(11, "club"),
                    deck.Card(12, "club"),
                    deck.Card(13, "club"),
                    deck.Card(1, "spade"),
                ],
                expected="Straight",
                num_cards=5,
            ),
            parameterized.param(
                "Three of a Kind",
                cards=[
                    deck.Card(9, "heart"),
                    deck.Card(9, "club"),
                    deck.Card(9, "club"),
                    deck.Card(1, "club"),
                    deck.Card(6, "spade"),
                ],
                expected="Three of a Kind",
                num_cards=3,
            ),
            parameterized.param(
                "Three of a Kind 4 cards",
                cards=[
                    deck.Card(9, "heart"),
                    deck.Card(1, "club"),
                    deck.Card(9, "club"),
                    deck.Card(9, "club"),
                ],
                expected="Three of a Kind",
                num_cards=3,
            ),
            parameterized.param(
                "Three of a Kind 3 cards",
                cards=[
                    deck.Card(9, "club"),
                    deck.Card(9, "club"),
                    deck.Card(9, "club"),
                ],
                expected="Three of a Kind",
                num_cards=3,
            ),
            parameterized.param(
                "Two Pair",
                cards=[
                    deck.Card(10, "heart"),
                    deck.Card(10, "club"),
                    deck.Card(13, "club"),
                    deck.Card(4, "club"),
                    deck.Card(4, "spade"),
                ],
                expected="Two Pair",
                num_cards=4,
            ),
            parameterized.param(
                "Two Pair 4 cards",
                cards=[
                    deck.Card(10, "heart"),
                    deck.Card(4, "heart"),
                    deck.Card(10, "heart"),
                    deck.Card(4, "heart"),
                ],
                expected="Two Pair",
                num_cards=4,
            ),
            parameterized.param(
                "Pair",
                cards=[
                    deck.Card(8, "club"),
                    deck.Card(8, "club"),
                    deck.Card(13, "club"),
                    deck.Card(12, "club"),
                    deck.Card(11, "spade"),
                ],
                expected="Pair",
                num_cards=2,
            ),
            parameterized.param(
                "Pair 4 cards",
                cards=[
                    deck.Card(8, "club"),
                    deck.Card(13, "club"),
                    deck.Card(8, "club"),
                    deck.Card(12, "club"),
                ],
                expected="Pair",
                num_cards=2,
            ),
            parameterized.param(
                "Pair 3 cards",
                cards=[
                    deck.Card(12, "club"),
                    deck.Card(8, "heart"),
                    deck.Card(8, "spade"),
                ],
                expected="Pair",
                num_cards=2,
            ),
            parameterized.param(
                "Pair 2 cards",
                cards=[
                    deck.Card(8, "heart"),
                    deck.Card(8, "spade"),
                ],
                expected="Pair",
                num_cards=2,
            ),
            parameterized.param(
                "High Card",
                cards=[
                    deck.Card(13, "heart"),
                    deck.Card(8, "heart"),
                    deck.Card(7, "spade"),
                    deck.Card(6, "spade"),
                    deck.Card(5, "spade"),
                ],
                expected="High Card",
                num_cards=1,
            ),
            parameterized.param(
                "High Card 4 cards",
                cards=[
                    deck.Card(8, "heart"),
                    deck.Card(7, "heart"),
                    deck.Card(13, "heart"),
                    deck.Card(2, "heart"),
                ],
                expected="High Card",
                num_cards=1,
            ),
            parameterized.param(
                "High Card 3 cards",
                cards=[
                    deck.Card(7, "heart"),
                    deck.Card(10, "diamond"),
                    deck.Card(2, "club"),
                ],
                expected="High Card",
                num_cards=1,
            ),
            parameterized.param(
                "High Card 2 cards",
                cards=[
                    deck.Card(2, "heart"),
                    deck.Card(10, "diamond"),
                ],
                expected="High Card",
                num_cards=1,
            ),
            parameterized.param(
                "High Card 1 card",
                cards=[
                    deck.Card(10, "diamond"),
                ],
                expected="High Card",
                num_cards=1,
            ),
        ]
    )
    def test_get_scoring_hand(self, _, cards: list[deck.Card], expected: str, num_cards: int):
        """Test that certain card combos return the correct scoring hand."""
        score, cards_that_scored = self.game.get_scoring_hand(cards)
        self.assertEqual(score.scoring_hand, expected)
        self.assertEqual(len(cards_that_scored), num_cards)
