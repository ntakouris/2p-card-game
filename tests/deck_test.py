from re import A
from game.deck import Deck


def test_deck_init():
    deck = Deck()

    assert len(deck.cards) == 52
    assert len(set(deck.cards)) == 52  # no duplicates


def test_deck_shuffle():
    deck = Deck()
    deck.shuffle()

    assert len(deck.cards) == 52
    assert len(set(deck.cards)) == 52  # no duplicates


def test_deck_split_into_halfs():
    deck = Deck()

    pt_a, pt_b = deck.split_into_half()

    assert len(pt_a) == 26
    assert len(pt_a) == len(pt_b)

    assert len(set(pt_a + pt_b)) == 26 * 2  # no duplicates
