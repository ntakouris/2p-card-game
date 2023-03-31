class Card:
    def __init__(self, number: int) -> None:
        assert number >= 1, f"Card number {number} should be >= 1"
        assert number <= 52, f"Card number {number} should be <= 52"

        self._number = number

    def __gt__(self, other) -> bool:
        assert isinstance(other, Card), f"Can't compare {type(self)} and {type(other)}"
        return self._number > other._number
