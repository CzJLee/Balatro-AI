"""Brute force calculations."""

import mini_balatro
import deck
import itertools
from tqdm.auto import tqdm


def find_max_scoring_hand(
    game: mini_balatro.Game, cards: list[deck.Card], verbose: bool = True
) -> tuple[int, list[deck.Card], mini_balatro.Score]:
    """Find the set of 5 cards that scores the most points.

    Args:
        cards: The list of cards to evaluate. Can be more than 5.

    Returns:
        A tuple of the score and the cards that score the most points.
    """
    max_score = 0
    best_cards = []
    best_scoring_hand = None

    cards_to_score = itertools.combinations(cards, 5)
    for cards in (cards_to_score):
        hand_score, scoring_hand, _ = game.score_hand(list(cards))
        if hand_score > max_score:
            max_score = hand_score
            best_cards = cards
            best_scoring_hand = scoring_hand

    if verbose:
        print(f"Max score: {max_score}")
        print(f"Best cards: {best_cards}")
        print(f"Scoring hand: {best_scoring_hand.scoring_hand}")

    return max_score, best_cards, best_scoring_hand


if __name__ == "__main__":
    game = mini_balatro.Game(seed=3)
    for i in range(100):
        game.new_round(seed=i, deal_hand=False)

        # Play a round using the first 3 discards, then play a hand, then play hands to discard, and play the last hand.
        # The first hand considers a minimum of 8 + 4*3 cards. Only consider discards of 4 in case we are hunting for one last card. (i.e. already have 4 that we need).
        # The second hand assume that we start with nothing. We then draw 5 from the deck. Then we can waste 2 more hands. So assume we can consider 5 + 4*2 cards.

        first_set_of_cards = []
        for _ in range(20):
            first_set_of_cards.append(game.deck.draw())
        first_max_score, first_best_cards, first_scoring_hand = find_max_scoring_hand(
            game=game, cards=first_set_of_cards, verbose=False
        )

        second_set_of_cards = []
        for _ in range(13):
            second_set_of_cards.append(game.deck.draw())
        second_max_score, second_best_cards, second_scoring_hand = find_max_scoring_hand(
            game=game, cards=second_set_of_cards, verbose=False
        )

        total_score = first_max_score + second_max_score
        print(f"Seed: {i} - Total score: {total_score}")
