import dataclasses
import random
from typing import Literal

import colorama

# Possible card suits.
SUIT = {
    "heart": "♥️",
    "diamond": "♦️",
    "club": "♣️",
    "spade": "♠️",
}

# Possible card ranks.
RANK = {
    1: "A",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
}

# Chip values for each card rank.
CHIP_VALUE = {
    1: 11,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 10,
    12: 10,
    13: 10,
}

# Sorted ranking of card ranks.
SORT_RANK = {
    1: 1,
    13: 2,
    12: 3,
    11: 4,
    10: 5,
    9: 6,
    8: 7,
    7: 8,
    6: 9,
    5: 10,
    4: 11,
    3: 12,
    2: 13,
}

# Sorted ranking of card suits.
SORT_SUIT = {
    "spade": 1,
    "heart": 2,
    "club": 3,
    "diamond": 4,
}


@dataclasses.dataclass
class Card:
    """Standard playing card."""

    suit: Literal["heart", "diamond", "club", "spade"]
    rank: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    chip_value: int
    mult_value: int

    def __repr__(self):
        if self.suit == "spade":
            color = colorama.Fore.WHITE
        elif self.suit == "heart":
            color = colorama.Fore.RED
        elif self.suit == "club":
            color = colorama.Fore.GREEN
        elif self.suit == "diamond":
            color = colorama.Fore.YELLOW
        else:
            color = colorama.Fore.RESET
        return f"{color}{RANK[self.rank]}{SUIT[self.suit]}{colorama.Style.RESET_ALL}"


class Stack:
    """Stack of cards."""

    def __init__(self, cards: list[Card] | None = None):
        if cards is None:
            cards = []
        self.cards: list[Card] = cards

    def __len__(self) -> int:
        return len(self.cards)

    def __repr__(self) -> str:
        return str(self.cards)

    def __getitem__(self, index: int) -> Card:
        return self.cards[index]

    def __contains__(self, card: Card) -> bool:
        return card in self.cards

    def __iter__(self):
        return iter(self.cards)

    def extend(self, cards: list[Card]) -> None:
        self.cards.extend(cards)

    def shuffle(self) -> None:
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def sort(self, by: Literal["rank", "suit"] = "rank") -> None:
        """Sort the deck."""
        if by == "rank":
            self.cards.sort(key=lambda x: (SORT_RANK[x.rank], SORT_SUIT[x.suit]))
        elif by == "suit":
            self.cards.sort(key=lambda x: (SORT_SUIT[x.suit], SORT_RANK[x.rank]))
        else:
            raise ValueError(f"Invalid sort by: {by}")

    def append(self, card: Card) -> None:
        """Append a card to the stack."""
        self.cards.append(card)


class Deck(Stack):
    """A standard deck of 52 cards."""

    def __init__(self, cards: list[Card] | None = None, seed: int | None = None):
        super().__init__(cards)
        self.cards = [
            Card(suit, rank, CHIP_VALUE[rank], 0) for suit in SUIT for rank in RANK
        ]
        random.seed(seed)
        self.shuffle()

    def draw(self) -> Card:
        """Draw a card from the deck."""
        return self.cards.pop()


class Hand(Stack):
    def __init__(self, cards: list[Card] | None = None):
        super().__init__(cards)

    def remove(self, card: Card):
        """Remove a card from the hand."""
        self.cards.remove(card)

    def pop(self, index: int) -> Card:
        """Pop a card from the hand by index."""
        return self.cards.pop(index)
