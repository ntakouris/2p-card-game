from .deck import Deck


class Game:
    def __init__(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()

        self.p1_cards, self.p2_cards = self.deck.split_into_half()
        self.p1_score, self.p2_score = 0, 0

    def play_round(self):
        p1_card = self.p1_cards.pop(0)
        p2_card = self.p2_cards.pop(0)

        print(f"Player 1: {p1_card} | Player 2: {p2_card}", end=" ")

        if p1_card > p2_card:
            print("--> Player 1 wins this round.")
            self.p1_score += 1
        elif p2_card > p1_card:
            print("--> Player 2 wins this round.")
            self.p2_score += 1

    def play_game(self):
        while len(self.p1_cards) > 0 and len(self.p2_cards) > 0:
            self.play_round()

        print(f"Final Score - Player 1: {self.p1_score} | Player 2: {self.p2_score}")

        if self.p1_score > self.p2_score:
            print("Player 1 wins the game!")
        elif self.p2_score > self.p1_score:
            print("Player 2 wins the game!")
        else:
            print("The game is a draw!")
