import pytest

from game.card import Card


def test_card_number_gt_or_eq_1():
    with pytest.raises(AssertionError, match="Card number 0 should be >= 1"):
        Card(0)

    with pytest.raises(AssertionError, match="Card number -1 should be >= 1"):
        Card(-1)

    c = Card(1)
    assert c


def test_card_number_le_or_eq_52():
    with pytest.raises(AssertionError, match="Card number 53 should be <= 52"):
        Card(53)

    with pytest.raises(AssertionError, match="Card number 100 should be <= 52"):
        Card(100)

    c = Card(52)
    assert c


def test_card_gt_lt_comparison():
    c1 = Card(1)

    c2 = Card(20)

    c3 = Card(52)

    assert c1 < c2
    assert c2 < c3

    assert c2 > c1
    assert c3 > c2

    assert c1 < c3
    assert c3 > c1
