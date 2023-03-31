import pytest

from game.card import Card


def test_card_str():
    assert f"{Card(5)}" == "5"


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
    assert Card(1) < Card(20)
    assert Card(20) < Card(52)

    assert Card(20) > Card(1)
    assert Card(52) > Card(20)

    assert Card(1) < Card(52)
    assert Card(52) > Card(1)

    with pytest.raises(
        AssertionError, match="Can't compare <class 'game.card.Card'> and <class 'str'>"
    ):
        Card(1) > "i am a str"


def test_card_hash():
    card_set = set([Card(2), Card(2), Card(3)])
    assert len(card_set) == 2

    assert Card(2) in card_set
    assert Card(3) in card_set


def test_card_eq():
    assert not Card(2) == Card(3)
    assert Card(2) == Card(2)

    with pytest.raises(
        AssertionError, match="Can't compare <class 'game.card.Card'> and <class 'str'>"
    ):
        Card(1) == "i am a str"
