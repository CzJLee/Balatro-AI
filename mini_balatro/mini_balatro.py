import collections
import dataclasses
from collections.abc import Collection

import deck


@dataclasses.dataclass
class Score:
    chip_value: int
    mult_value: int
    scoring_hand: str

    def total(self) -> int:
        return self.chip_value * self.mult_value


class ScoringHand:
    high_card = Score(5, 1, "High Card")
    pair = Score(10, 2, "Pair")
    two_pair = Score(20, 2, "Two Pair")
    three_of_a_kind = Score(30, 3, "Three of a Kind")
    straight = Score(30, 4, "Straight")
    flush = Score(35, 4, "Flush")
    full_house = Score(40, 4, "Full House")
    four_of_a_kind = Score(60, 7, "Four of a Kind")
    straight_flush = Score(100, 8, "Straight Flush")
    five_of_a_kind = Score(120, 12, "Five of a Kind")
    flush_house = Score(140, 14, "Flush House")
    flush_five = Score(160, 16, "Flush Five")


class Game:
    def __init__(self, seed: int | None = None):
        self.deck: deck.Deck = None
        self.hand: deck.Hand = None
        self.round_score: int = 0
        self.target_score: int = 600
        self.hands: int = 4
        self.hand_limit: int = 8
        self.discards: int = 3
        self.ante: int = 1
        self.round: int = 1
        self.money: int = 4

        self.seed = seed

    def deal_hand(self):
        """Draws cards from the deck up to the hand limit."""
        while len(self.hand) < self.hand_limit:
            self.hand.append(self.deck.draw())

    def new_round(self):
        """Sets the game state to a new round."""
        self.deck = deck.Deck(seed=self.seed)
        self.hand = deck.Hand()
        self.round_score = 0
        self.target_score = 600
        self.hands = 4
        self.discards = 3
        self.deal_hand()
        self.hand.sort()

    def check_target_score(self) -> bool:
        """After playing a hand, check to see if the target score has been reached."""
        if self.round_score >= self.target_score:
            print("Blind Complete!")
            self.new_round()
            self.round += 1
            return True
        elif self.hands <= 0:
            print("Game Over!")
            self.new_round()
            self.round = 0
            return True
        return False

    def _confirm_text(
        self, cards: deck.Stack, top_text: str, bottom_text: str, pad: int = 10
    ):
        top_string = [f"{top_text}:".ljust(pad)]
        bottom_string = [f"{bottom_text}:".ljust(pad)]
        for card in self.hand:
            if card in cards:
                top_string.append(f"{card}  ")
                bottom_string.append("    ")
            else:
                top_string.append("    ")
                bottom_string.append(f"{card}  ")
        print()
        print("".join(top_string))
        print("".join(bottom_string))

    def redraw_hand(self) -> list[deck.Card]:
        """Draw cards to the hand until full.

        Returns:
            List of new cards drawn.
        """
        new_cards = []
        for _ in range(self.hand_limit - len(self.hand)):
            new_cards.append(self.deck.draw())
        self.hand.extend(new_cards)
        self.hand.sort()

        return new_cards

    def partition(
        self, card_indices: Collection[int]
    ) -> tuple[list[deck.Card], list[deck.Card]]:
        """Partition the hand into two groups of cards."""
        cards_selected = []
        cards_remaining = []
        for i, card in enumerate(self.hand):
            if i in card_indices:
                cards_selected.append(card)
            else:
                cards_remaining.append(card)

        return cards_selected, cards_remaining

    def discard_cards(
        self, card_indices: Collection[int], confirm: bool = True
    ) -> None:
        if self.discards <= 0:
            raise ValueError("No discards remaining.")
        self.discards -= 1

        cards_to_discard, cards_to_keep = self.partition(card_indices)

        if confirm:
            self._confirm_text(cards_to_discard, "DISCARD", "KEEP")

        self.hand = deck.Hand(cards_to_keep)

        # Draw new cards
        new_cards = self.redraw_hand()

        if confirm:
            self._confirm_text(new_cards, "NEW", "OLD")

        self.hand = deck.Hand(cards_to_keep)

    def play_hand(self, card_indices: Collection[int], confirm: bool = True) -> None:
        """Plays a hand of cards from the hand, return the score."""
        if self.hands <= 0:
            raise ValueError("No hands remaining.")
        self.hands -= 1

        cards_to_play, cards_to_keep = self.partition(card_indices)

        if confirm:
            self._confirm_text(cards_to_play, "PLAY", "KEEP")

        # Remove played cards from hand
        self.hand = deck.Hand(cards_to_keep)

        # Calculate score
        score, cards_that_scored = self.get_scoring_hand(cards_to_play)
        for card in cards_that_scored:
            score.chip_value += card.chip_value
            score.mult_value += card.mult_value

        self.round_score += score.total()

        # Print score details.
        print()
        print(f"{score.scoring_hand}: {cards_to_play}")
        print(f"Cards scored: {cards_that_scored}")
        print(f"Score: {score.chip_value} x {score.mult_value} = {score.total()}")
        print(f"Total Score: {self.round_score} / {self.target_score}")

        round_complete = self.check_target_score()
        if round_complete:
            return

        # Draw new cards
        new_cards = self.redraw_hand()

        if confirm:
            self._confirm_text(new_cards, "NEW", "OLD")

    def _is_flush(self, cards: list[deck.Card]) -> bool:
        """Check if a played hand is a flush."""
        suits = collections.Counter([card.suit for card in cards])
        return len(suits) == 1 and len(cards) == 5

    def _is_straight(self, cards: list[deck.Card]) -> bool:
        """Check if a played hand is a straight."""
        ranks = collections.Counter([card.rank for card in cards])
        if len(ranks) < 5:
            return False

        sorted_ranks = sorted([deck.SORT_RANK[card.rank] for card in cards])
        if 1 in sorted_ranks and 13 in sorted_ranks:
            # Check for A, 2, 3, 4, 5.
            sorted_ranks.remove(1)
            sorted_ranks.append(14)
        return sorted_ranks[-1] - sorted_ranks[0] == 4

    def get_scoring_hand(self, cards: list[deck.Card]) -> tuple[Score, list[deck.Card]]:
        """Get the type of scoring hand for the played hand.

        Args:
            cards: The cards played in the hand.

        Returns:
            The type of scoring hand and the cards that scored in the hand.
        """
        if not cards:
            raise ValueError("Cannot calculate score for empty hand.")
        elif len(cards) > 5:
            raise ValueError("Cannot play more than 5 cards.")

        cards.sort()
        ranks = collections.Counter([card.rank for card in cards])

        # Check for flush
        flush = self._is_flush(cards)
        # Check for straight
        straight = self._is_straight(cards)

        # Check for pairs, working in descending priority.
        rank_counts = sorted(ranks.values(), reverse=True)
        if rank_counts[0] == 5:
            if flush:
                return ScoringHand.flush_five, cards
            else:
                return ScoringHand.five_of_a_kind, cards
        elif rank_counts[0] == 4:
            return ScoringHand.four_of_a_kind, self._largest_set(cards)
        elif len(cards) == 5 and rank_counts[0] == 3 and rank_counts[1] == 2:
            if flush:
                return ScoringHand.flush_house, cards
            else:
                return ScoringHand.full_house, cards
        elif flush:
            if straight:
                return ScoringHand.straight_flush, cards
            else:
                return ScoringHand.flush, cards
        elif straight:
            return ScoringHand.straight, cards
        elif rank_counts[0] == 3:
            return ScoringHand.three_of_a_kind, self._largest_set(cards)
        elif len(cards) >= 4 and rank_counts[0] == 2 and rank_counts[1] == 2:
            return ScoringHand.two_pair, self._two_pair(cards)
        elif rank_counts[0] == 2:
            return ScoringHand.pair, self._largest_set(cards)
        else:
            return ScoringHand.high_card, [cards[0]]

    def _largest_set(self, cards: list[deck.Card]) -> list[deck.Card]:
        """Return the cards that form the largest pair.

        Either a pair, three of a kind, or four of a kind.
        """
        cards.sort()
        ranks = collections.Counter([card.rank for card in cards])
        most_common = ranks.most_common(1)
        most_common_rank = most_common[0][0]
        return [card for card in cards if card.rank == most_common_rank]

    def _two_pair(self, cards: list[deck.Card]) -> list[deck.Card]:
        """Return the cards that form the two pair."""
        cards.sort()
        ranks = collections.Counter([card.rank for card in cards])
        most_common = ranks.most_common(2)
        selected_ranks = [most_common[0][0], most_common[1][0]]
        return [card for card in cards if card.rank in selected_ranks]
